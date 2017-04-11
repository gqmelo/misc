
set -gx FZF_DEFAULT_OPTS '--bind alt-j:preview-page-down --bind alt-k:preview-page-up --bind ctrl-l:select-all --bind ctrl-n:deselect-all --bind "enter:execute(echo -n {+} | xsel -i -b)+accept"'
set -gx FZF_CTRL_T_OPTS '--bind "enter:execute(echo -n {+} | xargs copy-path-to-clipboard)+accept"'
fzf_key_bindings

# Show history with fzf and copy the selection to clipboard
bind \er "history | fzf -m --bind enter:accept | xsel -i -b"

set read_command "read -l result; and commandline -- \$result; commandline -f repaint"

# Binds for git refs
bind \cg\cb "git fshow branch | $read_command"
bind \cg\cr "git fshow branch -r | $read_command"
bind \cg\ct "git fshow tag --sort -version:refname | $read_command"
bind \cg\ch "git fshow lgg --all | $read_command"
