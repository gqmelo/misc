set -gx PATH ~/workspace/misc/bin $PATH
eval (python -m virtualfish)
complete --command mu --wraps git
