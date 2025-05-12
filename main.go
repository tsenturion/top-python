if условие {
    // блок кода
} else if другое_условие {
    // блок кода
} else {
    // блок кода
}
if условие {
    // блок кода
} else if другое_условие {
    // блок кода
} else {
    // блок кода
}
age := 20
if age < 18 {
    fmt.Println("Несовершеннолетний")
} else if age < 65 {
    fmt.Println("Взрослый")
} else {
    fmt.Println("Пожилой")
}
if x > 0 {
    fmt.Println("Положительное число")
}
if (x > 0) { // ❌

if condition {
    // тело условия
}

if x := getValue(); x > 10 {
    fmt.Println("Значение больше 10")
}

switch day := 3; day {
case 1:
    fmt.Println("Понедельник")
case 2:
    fmt.Println("Вторник")
case 3:
    fmt.Println("Среда")
default:
    fmt.Println("Другой день")
}

switch {
case x > 0:
    fmt.Println("Положительное")
case x < 0:
    fmt.Println("Отрицательное")
default:
    fmt.Println("Ноль")
}

if (x > 0) { // ❌ Ошибка

if x > 0 { // ✅ Правильно

if x > 0
    fmt.Println("Да") // ❌

if x := getValue(); x > 10 {
    fmt.Println(x)
}

// Здесь x больше не существует ❌

for i := 1; i <= 10; i++ {
    fmt.Println(i)
}

i := 1
for i <= 10 {
    fmt.Println(i)
    i++
}
for x != 0 {
    // выполняем действия
}

for {
    // бесконечный цикл
}

for {
    var input string
    fmt.Print("Введите 'стоп' для выхода: ")
    fmt.Scanln(&input)

    if input == "стоп" {
        break
    }

    fmt.Println("Вы ввели:", input)
}

for i := 1; i <= 10; i++ {
    if i%2 == 0 {
        continue
    }
    fmt.Println(i) // напечатает только нечётные числа
}
