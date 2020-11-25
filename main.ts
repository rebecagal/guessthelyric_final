input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Yes)
    songAnswers()
    music.playTone(659, music.beat(BeatFraction.Whole))
    music.playTone(698, music.beat(BeatFraction.Whole))
    sprite = game.createSprite(2, 2)
    sprite.turn(Direction.Right, 45)
    game.addScore(1)
    basic.showNumber(game.score())
    if (game.score() == 6) {
        basic.showString("WINNER")
        game.setScore(0)
    } else if (game.score() <= 5) {
        basic.showString("NEXT SONG")
    }
})
function songAnswers () {
    if (Song == 1) {
        basic.showString("positions - Ariana Grande")
    } else if (Song == 2) {
        basic.showString("Super Bass - Nicki Minaj")
    } else if (Song == 3) {
        basic.showString("bad guy - Billie Eilish")
    } else if (Song == 4) {
        basic.showString("When I Was Your Man - Bruno Mars")
    } else if (Song == 5) {
        basic.showString("Sofia - Clairo")
    } else if (Song == 6) {
        basic.showString("Heather - Conan Gray")
    } else if (Song == 7) {
        basic.showString("New Rules - Dua Lipa")
    } else if (Song == 8) {
        basic.showString("Golden - Harry Styles")
    } else if (Song == 9) {
        basic.showString("Baby - Justin Bieber")
    } else if (Song == 10) {
        basic.showString("Last Friday Night (T.G.I.F) - Katy Perry")
    } else if (Song == 11) {
        basic.showString("Rain On Me - Lady Gaga & Ariana Grande")
    } else if (Song == 12) {
        basic.showString("Steal My Girl - One Direction")
    } else if (Song == 13) {
        basic.showString("In My Blood - Shawn Mendes")
    } else if (Song == 14) {
        basic.showString("Shake It Off - Taylor Swift")
    } else if (Song == 15) {
        basic.showString("Blinding Lights - The Weeknd")
    }
}
input.onButtonPressed(Button.AB, function () {
    Song = randint(1, 15)
    selectSong()
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.No)
    songAnswers()
    music.playTone(175, music.beat(BeatFraction.Whole))
    music.playTone(131, music.beat(BeatFraction.Whole))
    sprite.turn(Direction.Left, 45)
    basic.showNumber(game.score())
    if (game.score() == 6) {
        basic.showString("WINNER")
        game.setScore(0)
    } else if (game.score() <= 5) {
        basic.showString("NEXT SONG")
    }
})
function selectSong () {
    if (Song == 1) {
        basic.showString("Cookin in the kitchen and in the")
    } else if (Song == 2) {
        basic.showString("the boys with the boomin' system")
    } else if (Song == 3) {
        basic.showString("So you're a tough guy, like it really rough guy")
    } else if (Song == 4) {
        basic.showString("I should have bought you flowers and")
    } else if (Song == 5) {
        basic.showString("if we tried, if only to say, you're mine")
    } else if (Song == 6) {
        basic.showString("I'm not even half as pretty")
    } else if (Song == 7) {
        basic.showString("You know he's only callin cause he's drunk and alone")
    } else if (Song == 8) {
        basic.showString("You're scared because hearts get broken")
    } else if (Song == 9) {
        basic.showString("My first love broke my heart for the first time")
    } else if (Song == 10) {
        basic.showString("glitter all over the room, pink flamingos in the pool")
    } else if (Song == 11) {
        basic.showString("Livin in a world where no one's innocent")
    } else if (Song == 12) {
        basic.showString("Find another one cause she belongs to me!")
    } else if (Song == 13) {
        basic.showString("The walls are caving in, sometimes I feel like giving up")
    } else if (Song == 14) {
        basic.showString("Cause the players gonna play, play, play, play, play")
    } else if (Song == 15) {
        basic.showString("The sun light up the sky so I hit the road in overdrive")
    }
}
let Song = 0
let sprite: game.LedSprite = null
music.playMelody("E E F F G A B C5 ", 120)
basic.showIcon(IconNames.Chessboard)
basic.showIcon(IconNames.Diamond)
basic.showIcon(IconNames.SmallDiamond)
game.setScore(0)
