package adgvkty

import "fmt"

// CalculateHighMath ...
func CalculateHighMath() {
	var value int = 1489
	var firstNumber int
	var secondNumber int

	firstNumber = value % 10

	for {
		value = value / 10
		if value/10 == 0 {
			secondNumber = value % 10
			break
		}
	}

	fmt.Println(firstNumber, secondNumber)
}
