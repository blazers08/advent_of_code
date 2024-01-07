import java.io.File
import java.io.InputStream

fun formDigit(input: String): Int {
    var number: Int
    val digitStrings: List<Int> = input.mapNotNull { character ->
        character.toString().toIntOrNull()
    }

    (digitStrings.size == 1).run {
        number = digitStrings.first() * 11
    }
    number = digitStrings.first() * 10 + digitStrings.last() * 1

    return number
}

fun sum(number: Int): Int {
    var total: Int = 0
    total += number
    return total
}

fun main(args: Array<String>) {
    var total: Int = 0

    val inputStream: InputStream = File("src/main/resources/input.in").absoluteFile.inputStream()
    inputStream.bufferedReader().use {
        it.forEachLine { text ->
            total += sum(formDigit(text))
        }
    }
    println(total)
}