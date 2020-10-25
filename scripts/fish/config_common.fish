. ~/miniconda3/etc/fish/conf.d/conda.fish

if not contains ~/workspace/misc/bin $PATH
    set -gx PATH ~/workspace/misc/bin $PATH
end

if not contains ~/bin $PATH
    set -gx PATH ~/bin $PATH
end

if not contains ~/.cargo/bin $PATH
    set -gx PATH ~/.cargo/bin $PATH
end

complete --command mu --wraps git
