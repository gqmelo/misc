
set -gx FZF_DEFAULT_OPTS '--bind alt-j:preview-page-down --bind alt-k:preview-page-up --bind ctrl-l:select-all --bind ctrl-n:deselect-all --bind "enter:execute(echo {+} | xsel -b)+accept"'
fzf_key_bindings

# Show history with fzf e copy the selection to clipboard
bind \er "history | fzf -m | xsel -b"