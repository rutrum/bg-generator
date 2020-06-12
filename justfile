alias r := run
run:
    python3 gen.py
    just bg

pic:
    sxiv background.png &

alias w := watch
watch: 
    watchexec --ignore *.png -- just r

bg:
    feh --bg-fill background.png
