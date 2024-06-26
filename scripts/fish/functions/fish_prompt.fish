function fish_prompt --description 'Write out the prompt'
	set -l last_status $status
	# Show notification if the last command took too much time
	long_command_notify

	if set -q VIRTUAL_ENV
		set virtualenv (set_color -b blue white) "(" (basename "$VIRTUAL_ENV") ")" (set_color normal)" "
	end

	# Just calculate this once, to save a few cycles when displaying the prompt
	if not set -q __fish_prompt_hostname
		set -g __fish_prompt_hostname (hostname|cut -d . -f 1)
	end

	set -l normal (set_color normal)

	# Hack; fish_config only copies the fish_prompt function (see #736)
	if not set -q -g __fish_classic_git_functions_defined
		set -g __fish_classic_git_functions_defined

		function __fish_repaint_user --on-variable fish_color_user --description "Event handler, repaint when fish_color_user changes"
			if status --is-interactive
				commandline -f repaint ^/dev/null
			end
		end

		function __fish_repaint_host --on-variable fish_color_host --description "Event handler, repaint when fish_color_host changes"
			if status --is-interactive
				commandline -f repaint ^/dev/null
			end
		end

		function __fish_repaint_status --on-variable fish_color_status --description "Event handler; repaint when fish_color_status changes"
			if status --is-interactive
				commandline -f repaint ^/dev/null
			end
		end

		function __fish_repaint_bind_mode --on-variable fish_key_bindings --description "Event handler; repaint when fish_key_bindings changes"
			if status --is-interactive
				commandline -f repaint ^/dev/null
			end
		end

		# initialize our new variables
		if not set -q __fish_classic_git_prompt_initialized
			set -qU fish_color_user; or set -U fish_color_user -o green
			set -qU fish_color_host; or set -U fish_color_host -o cyan
			set -qU fish_color_status; or set -U fish_color_status red
			set -U __fish_classic_git_prompt_initialized
		end
	end

	# fish version available on Ubuntu 16.04 has no __fish_vcs_prompt function
	if not functions -q __fish_vcs_prompt
		functions -c __fish_git_prompt __fish_vcs_prompt
	end

	set -l color_cwd
	set -l prefix
	switch $USER
	case root toor
		if set -q fish_color_cwd_root
			set color_cwd $fish_color_cwd_root
		else
			set color_cwd $fish_color_cwd
		end
		set suffix '#'
	case '*'
		set color_cwd $fish_color_cwd
		set suffix '>'
	end

	set -l prompt_status
	if test $last_status -ne 0
		set prompt_status ' ' (set_color $fish_color_status) "[$last_status]" "$normal"
	end

	set -l icon ""
	if string match -q -- "dev-dsk*" $__fish_prompt_hostname
		set icon (set_color $fish_color_host)"[REMOTE] "
	end

	set -g __fish_git_prompt_show_informative_status 1
	set -g __fish_git_prompt_showcolorhints 1

	echo -n -s (set_color normal) $virtualenv [(date +%X)] " $icon" (set_color $fish_color_user) "$USER" $normal @ (set_color $fish_color_host) "$__fish_prompt_hostname" $normal ' ' (set_color $color_cwd) $PWD $normal (__fish_vcs_prompt) $normal $prompt_status "
> "
end
