if not contains ~/workspace/misc/bin $fish_user_paths
    set -U fish_user_paths ~/workspace/misc/bin $fish_user_paths
end
eval (python -m virtualfish)
complete --command mu --wraps git
