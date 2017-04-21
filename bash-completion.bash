# xbmc-command bash completion

__xbmc-command ()
{
  local cur commands comm opt c

  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"
  commands="mute volume play-pause play-music next prev repeat shuffle"
  commands="${commands} system youtube twitch slideshow lyrics notification"
  commands="${commands} scan wake-on-lan rpc"
  opt="--host --port --timeout --help --version"

  for c in ${commands}; do
    case "${COMP_WORDS[@]}" in
      *"$c"*)
        comm="$c"
        break
        ;;
    esac
  done

  if [ -z $comm ]; then
    COMPREPLY=( $(compgen -W "$commands $opt" -- $cur) )
  else
    case "$comm" in
      mute)
        COMPREPLY=( $(compgen -W "yes no toggle --help" -- $cur) )
        ;;
      volume)
        COMPREPLY=( $(compgen -W "--help --increment --decrement --set" -- $cur) )
        ;;
      play-pause)
        COMPREPLY=( $(compgen -W "--help" -- $cur) )
        ;;
      play-music)
        COMPREPLY=( $(compgen -W "--help --artist --album --genre --dry" -- $cur) )
        ;;
      next)
        COMPREPLY=( $(compgen -W "--help" -- $cur) )
        ;;
      prev)
        COMPREPLY=( $(compgen -W "--help" -- $cur) )
        ;;
      repeat)
        COMPREPLY=( $(compgen -W "--help off one all cycle" -- $cur) )
        ;;
      shuffle)
        COMPREPLY=( $(compgen -W "--help yes no toggle" -- $cur) )
        ;;
      system)
        COMPREPLY=( $(compgen -W "--help quit shutdown reboot suspend hibernate infos" -- $cur) )
        ;;
      youtube)
        COMPREPLY=( $(compgen -W "--help --quaility 1080p 720p low" -- $cur) )
        ;;
      twitch)
        COMPREPLY=( $(compgen -W "--help --quaility 1080p60 1080p30 720p60 720p30 dialog" -- $cur) )
        ;;
      slideshow)
        COMPREPLY=( $(compgen -W "--help --dir --stop" -- $cur) )
        ;;
      lyrics)
        COMPREPLY=( $(compgen -W "--help" -- $cur) )
        ;;
      notification)
        COMPREPLY=( $(compgen -W "--help --title --message --time" -- $cur) )
        ;;
      scan)
        COMPREPLY=( $(compgen -W "--help --audio --video --dir" -- $cur) )
        ;;
      wake-on-lan)
        COMPREPLY=( $(compgen -W "--help --port" -- $cur) )
        ;;
      rpc)
        COMPREPLY=( $(compgen -W "--help --id" -- $cur) )
        ;;
    esac
  fi
}

complete -F __xbmc-command xbmc-command

# vim: ts=2 sts=2 sw=2 et:
