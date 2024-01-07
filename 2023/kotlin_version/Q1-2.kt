import java.io.File
import java.io.InputStream


fun formDigitFormLetters(input: String, map: Map<String, Int>): Int {
    val digitStrings = mutableListOf<Int>()
    var tmp = input

    while (tmp.isNotEmpty()) {
        if (tmp.first().isDigit()) {
            digitStrings.add(tmp.first().digitToInt())
        }

        map.forEach { (word, digit) ->
            if (tmp.startsWith(word)) {
                digitStrings.add(digit)
            }
        }
        tmp = tmp.drop(1)
    }
    return digitStrings.first() * 10 + digitStrings.last()
}

fun sum2(number: Int): Int {
    var total: Int = 0
    total += number
    return total
}

fun main(args: Array<String>) {
    var total: Int = 0
    val validDigits = mapOf(
        "one" to 1, "two" to 2, "three" to 3, "four" to 4,
        "five" to 5, "six" to 6, "seven" to 7, "eight" to 8, "nine" to 9
    )

    val inputStream: InputStream = File("src/main/resources/input.in").absoluteFile.inputStream()
    inputStream.bufferedReader().use {
        it.forEachLine{ text ->
            total += sum2(formDigitFormLetters(text, validDigits))
        }
        println(total)
    }
}