let x = 0
let timeout = 0
let start = 0
let animate = 0
input.onButtonPressed(Button.AB, () => {
    if (start == 1) {
        start = 0
        basic.showNumber(timeout)
    } else {
        start = 1
    }
})
// Increase timeout
input.onButtonPressed(Button.A, () => {
    animate = 0
    if (start == 0) {
        timeout += 1
        music.beginMelody(["c5:2"], MelodyOptions.Once)
    }
})
// Decrease timeout
input.onButtonPressed(Button.B, () => {
    animate = 0
    if (start == 0) {
        timeout += 0 - 1
        music.beginMelody(["c5:2"], MelodyOptions.Once)
        if (timeout < 1) {
            timeout = 1
        }
    }
})
// Animate LED matrix
function animate_LEDs()  {
    if (start == 1) {
        basic.plotLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    }
    for (let i = 0; i <= 25 - 1; i++) {
        y = Math.floor(i / 5)
        x = i % 5
        led.unplot(x, y)
        basic.pause(2400)
        // If user interrupts the timer, return immediately
        if (start == 0) {
            music.beginMelody(["g5:2"], MelodyOptions.Once)
            break
        }
    }
}
let y = 0
timeout = 1
animate = 1
basic.forever(() => {
    if (start == 1) {
        music.beginMelody(["g5:1"], MelodyOptions.Once)
        for (let i0 = 0; i0 < timeout; i0++) {
            animate_LEDs()
            // If user interrupts the timer, return immediately
            if (start == 0) {
                music.beginMelody(["a5:2"], MelodyOptions.Once)
                break
            }
        }
        music.beginMelody(["g5:30"], MelodyOptions.Once)
        start = 0
        animate = 1
    } else {
        if (animate == 1) {
            basic.showString("Timer")
        } else {
            basic.showNumber(timeout)
        }
    }
})
