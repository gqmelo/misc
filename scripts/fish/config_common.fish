. ~/miniconda3/etc/fish/conf.d/conda.fish

if not contains ~/workspace/misc/bin $PATH
    set -gx PATH ~/workspace/misc/bin $PATH
end

if not contains ~/bin $PATH
    set -gx PATH ~/bin $PATH
end

eval (python -m virtualfish)
complete --command mu --wraps git