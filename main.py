input.onButtonPressed(Button.AB, function () {
    let points2: number;
music.playMelody("E E F F G A B C5 ", 120)
    basic.showIcon(IconNames.Chessboard)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.SmallDiamond)
    for (let index = 0; index < 6; index++) {
        Song = randint(1, 15)
        selectSong()
        while (true) {
            if (input.buttonIsPressed(Button.A)) {
                break;
music.playTone(659, music.beat(BeatFraction.Whole))
                music.playTone(698, music.beat(BeatFraction.Whole))
                game.addScore(1)
                sprite = game.createSprite(2, 2)
                sprite.turn(Direction.Right, 45)
                points2 = points2 + 1
                continue;
            } else if (input.buttonIsPressed(Button.B)) {
                points2 = points2
                break;
music.playTone(175, music.beat(BeatFraction.Whole))
                music.playTone(131, music.beat(BeatFraction.Whole))
                sprite.turn(Direction.Left, 45)
                continue;
            }
        }
        basic.showNumber(game.score())
        if (game.score() < 5) {
            basic.showString("WINNER")
        } else if (game.score() > 4) {
            basic.showString("LOSER")
        }
        game.gameOver()
    }
    console.log(points2)
})
function selectSong () {
    if (Song == 1) {
        basic.showString("Cookin in the kitchen and I'm in the bedroom")
        game.startCountdown(30000)
        basic.showString("positions - Ariana Grande")
    } else if (Song == 2) {
        basic.showString("This one is for the boys with the boomin' system")
        game.startCountdown(30000)
        basic.showString("Super Bass - Nicki Minaj")
    } else if (Song == 3) {
        basic.showString("So you're a tough guy, like it really rough guy")
        game.startCountdown(30000)
        basic.showString("bad guy - Billie Eilish")
    } else if (Song == 4) {
        basic.showString("I should have bought you flowers and held your hand")
        game.startCountdown(30000)
        basic.showString("When I Was Your Man - Bruno Mars")
    } else if (Song == 5) {
        basic.showString("I think we could do it if we tried, if only to say, you're mine")
        game.startCountdown(30000)
        basic.showString("Sofia - Clairo")
    } else if (Song == 6) {
        basic.showString("Why would you ever kiss me? I'm not even half as pretty")
        game.startCountdown(30000)
        basic.showString("Heather - Conan Gray")
    } else if (Song == 7) {
        basic.showString("One: Don't pick up the phone. You know he's only callin cause he's drunk and alone")
        game.startCountdown(30000)
        basic.showString("New Rules - Dua Lipa")
    } else if (Song == 8) {
        basic.showString("I'm out of my head, and I know that you're scared because hearts get broken")
        game.startCountdown(30000)
        basic.showString("Golden - Harry Styles")
    } else if (Song == 9) {
        basic.showString("My first love broke my heart for the first time")
        game.startCountdown(30000)
        basic.showString("Baby - Justin Bieber")
    } else if (Song == 10) {
        basic.showString("There's a pounding in my head, glitter all over the room, pink flamingos in the pool")
        game.startCountdown(30000)
        basic.showString("Last Friday Night (T.G.I.F) - Katy Perry")
    } else if (Song == 11) {
        basic.showString("Livin in a world where no one's innocent, but at least we try")
        game.startCountdown(30000)
        basic.showString("Rain On Me - Lady Gaga & Ariana Grande")
    } else if (Song == 12) {
        basic.showString("Couple billion in the whole wide world. Find another one cause she belongs to me!")
        game.startCountdown(30000)
        basic.showString("Steal My Girl - One Direction")
    } else if (Song == 13) {
        basic.showString("Help me, it's like the walls are caving in, sometimes I feel like giving up")
        game.startCountdown(30000)
        basic.showString("In My Blood - Shawn Mendes")
    } else if (Song == 14) {
        basic.showString("Cause the players gonna play, play, play, play, play")
        game.startCountdown(30000)
        basic.showString("Shake It Off - Taylor Swift")
    } else if (Song == 15) {
        basic.showString("Cause I can see the sun light up the sky so I hit the road in overdrive, baby")
        game.startCountdown(30000)
        basic.showString("Blinding Lights - The Weeknd")
    }
}
let sprite: game.LedSprite = null
let Song = 0
let player = 0
let points = 0
game.setScore(player)
basic.forever(function () {
	
})
