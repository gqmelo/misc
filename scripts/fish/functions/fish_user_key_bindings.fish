
set -gx FZF_DEFAULT_OPTS '--bind alt-j:preview-page-down --bind alt-k:preview-page-up --bind ctrl-l:select-all --bind ctrl-n:deselect-all --bind "enter:execute(echo -n {+} | xsel -i -b)+accept"'
set -gx FZF_CTRL_T_OPTS '--bind "enter:execute(echo -n {+} | xargs copy-path-to-clipboard)+accept"'
fzf_key_bindings

# Show history with fzf and copy the selection to clipboard
bind \cx\cr "history | fzf -m --bind enter:accept | xsel -i -b"

set read_command "read -l result; and commandline -a \$result; commandline -f repaint"

function ffind --description 'Find files and do actions'
	set -l output (locate -Ai -0 / | fzf --read0 -0 -1 --expect=ctrl-o,ctrl-e,alt-c)
	set -l key (string join \n $output | head -n1)
	set -l file (string join \n $output | tail -n1)

	if [ $key = "alt-c" ]
		if test -d "$file"
			cd $file
		else
			cd (dirname "$file")
		end
		commandline -f repaint
	else if [ $key = "ctrl-o" ]
		xdg-open "$file"
	else if [ $key = "ctrl-e" ]
		vim "$file"
	end
end
bind \cx\ct ffind

function fuzzygrep --description 'Search for file contents'
	set -l output (ag --nobreak --noheading . | fzf --expect=ctrl-o,ctrl-e,alt-c)
	set -l key (string join \n $output | head -n1)
	set -l selected_item (string join \n $output | tail -n1)
	set -l file (string split ":" -- $selected_item)[1]
	set -l line (string split ":" -- $selected_item)[2]

	if [ $key = "alt-c" ]
		if test -d "$file"
			cd $file
		else
			cd (dirname "$file")
		end
		commandline -f repaint
	else if [ $key = "ctrl-o" ]
		xdg-open "$file"
	else if [ $key = "ctrl-e" ]
		vim "$file" +$line
	end
end
bind \cx\cf fuzzygrep

bind \e\j "prevd; commandline -f repaint"
bind \e\k "nextd; commandline -f repaint"

# Binds for git refs
bind \cg\cb "git fshow branch | $read_command"
bind \cg\cr "git fshow branch -a | $read_command"
bind \cg\ct "git fshow tag --sort -version:refname | $read_command"
bind \cg\ch "git fshow lgg --all | $read_command"

if test -e ~/workspace/Guilmelo/scripts/fish/fish_user_key_bindings.fish
	. ~/workspace/Guilmelo/scripts/fish/fish_user_key_bindings.fish
end
