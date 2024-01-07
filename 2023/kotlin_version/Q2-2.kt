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

fun determineNeededColor(input: List<Games>): Int {
    return input.sumOf { game ->
        val minCubesByColor = mutableMapOf(
            Color.RED to 0,
            Color.GREEN to 0,
            Color.BLUE to 0,
        )

        game.sets.forEach { set ->
            set.cubes.forEach { (color, amount) ->
                minCubesByColor[color] = maxOf(minCubesByColor[color]!!, amount)
            }
        }
        return@sumOf minCubesByColor.values.reduce(Int::times)
    }
}

fun main() {
    val games: List<Games>

    val inputStream: InputStream = File("src/main/resources/input.in").absoluteFile.inputStream()
    inputStream.bufferedReader().use {
        games = determinePossibleGame(it.readLines().toList())
        print(determineNeededColor(games))
    }
}