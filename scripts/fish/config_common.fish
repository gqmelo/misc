. $HOME/miniforge3/etc/fish/conf.d/conda.fish

if not contains $HOME/.local/bin $PATH
    set -gx PATH $HOME/.local/bin $PATH
end

if not contains $HOME/workspace/misc/bin $PATH
    set -gx PATH $HOME/workspace/misc/bin $PATH
end

if not contains $HOME/bin $PATH
    set -gx PATH $HOME/bin $PATH
end

if not contains $HOME/.cargo/bin $PATH
    set -gx PATH $HOME/.cargo/bin $PATH
end

# eval (python3 -m virtualfish)
complete --command mu --wraps git
