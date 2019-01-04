# echo-client.py
import subprocess
import trio


async def run(command, *, input=None, capture_output=False, **options):
    if input is not None:
        options['stdin'] = subprocess.PIPE

    if capture_output:
        options['stdout'] = options['stderr'] = subprocess.PIPE

    stdout_chunks = []
    stderr_chunks = []

    async with trio.subprocess.Process(command, **options) as proc:
        async def feed_input():
            async with proc.stdin:
                if input:
                    try:
                        await proc.stdin.send_all(input)
                    except trio.BrokenResourceError:
                        pass

    async def read_output(stream, chunks):
        async with stream:
            while True:
                chunk = await stream.receive_some(32768)
                if not chunk:
                    break
                chunks.append(chunk)

    async with trio.open_nursery() as nursery:
        if proc.stdin is not None:
            nursery.start_soon(feed_input)
        if proc.stdout is not None:
            nursery.start_soon(read_output, proc.stdout, stdout_chunks)
        if proc.stderr is not None:
            nursery.start_soon(read_output, proc.stderr, stderr_chunks)
        await proc.wait()

    stdout = b"".join(stdout_chunks) if proc.stdout is not None else None
    stderr = b"".join(stderr_chunks) if proc.stderr is not None else None

    if proc.returncode:
        raise subprocess.CalledProcessError(
            proc.returncode, proc.args, output=stdout, stderr=stderr
        )
    else:
        return subprocess.CompletedProcess(
            proc.args, proc.returncode, stdout, stderr
        )


async def parent():
    async with trio.open_nursery() as nursery:
        for i in range(20):
            print(f"parent: spawning subprocess '{i}'")
            nursery.start_soon(run, ["python", "echo_client.py"])


if __name__ == '__main__':
    trio.run(parent)
