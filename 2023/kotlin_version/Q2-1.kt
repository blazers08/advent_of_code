import java.io.File
import java.io.InputStream

data class Games(val id: Int, val sets: List<Set>)
data class Set(val cubes: MutableMap<Color, Int>)
enum class Color { RED, GREEN, BLUE }


fun determinePossibleGame(inputs: List<String>): List<Games> {
    return inputs.mapIndexed { index, input ->
        val sets = buildList {
            input.split(": ")[1].split("; ").forEach { set ->
                val current = Set(mutableMapOf())

                set.split(", ").forEach {
                    val (amount, color) = it.split(" ")

                    when (color) {
                        "red" -> current.cubes[Color.RED] = amount.toInt()
                        "green" -> current.cubes[Color.GREEN] = amount.toInt()
                        "blue" -> current.cubes[Color.BLUE] = amount.toInt()
                        else -> error("Invalid color")
                    }
                }
                this.add(current)
            }
        }
        return@mapIndexed Games(index + 1, sets)
    }
}

fun parseGames(input: List<Games>): Int {
    val maxCubesByColor = mapOf(
        Color.RED to 12,
        Color.GREEN to 13,
        Color.BLUE to 14
    )

    return input.sumOf { game ->
        game.sets.forEach { set ->
            if (set.cubes.any { (color, amount) -> amount > maxCubesByColor[color]!! })
                return@sumOf 0
        }
        return@sumOf game.id
    }
}

fun main(args: Array<String>) {
    val games: List<Games>

    val inputStream: InputStream = File("src/main/resources/input.in").absoluteFile.inputStream()
    inputStream.bufferedReader().use {
        games = determinePossibleGame(it.readLines().toList())
        print(parseGames(games))
    }
}