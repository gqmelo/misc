. ~/mambaforge/etc/fish/conf.d/conda.fish

if not contains ~/.local/bin $PATH
    set -gx PATH ~/.local/bin $PATH
end

if not contains ~/workspace/misc/bin $PATH
    set -gx PATH ~/workspace/misc/bin $PATH
end

if not contains ~/bin $PATH
    set -gx PATH ~/bin $PATH
end

if not contains ~/.cargo/bin $PATH
    set -gx PATH ~/.cargo/bin $PATH
end

# eval (python3 -m virtualfish)
complete --command mu --wraps git
