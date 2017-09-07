set -gx BRAZIL_CLI_BIN "/apollo/env/SDETools/bin"

. ~/workspace/misc/scripts/fish/config_custom.fish

if not contains $BRAZIL_CLI_BIN $fish_user_paths
  set -U fish_user_paths $BRAZIL_CLI_BIN $fish_user_paths
end

if not contains ~/.toolbox/bin $fish_user_paths
    set -U fish_user_paths ~/.toolbox/bin $fish_user_paths
end
