package com.mouredev.weeklychallenge2022

fun main() {

    area(Triangle(10.0, 5.0))
    area(Rectangle(5.0, 7.0))
    area(Square(4.0))
}

interface Polygon {

    fun area(): Double
    fun printArea()
}

data class Triangle(val base: Double, val height: Double): Polygon {

    override fun area(): Double {
        return (base * height) / 2
    }

    override fun printArea() {
        println("El área del triángulo es ${area()}")
    }
}

data class Rectangle(val length: Double, val width: Double): Polygon {

    override fun area(): Double {
        return length * width
    }

    override fun printArea() {
        println("El área del rectángulo es ${area()}")
    }
}

data class Square(val side: Double): Polygon {

    override fun area(): Double {
        return side * side
    }

    override fun printArea() {
        println("El área del cuadrado es ${area()}")
    }
}

private fun area(polygon: Polygon): Double {
    polygon.printArea()
    return polygon.area()
}
Footer
© 2023 GitHub, Inc.