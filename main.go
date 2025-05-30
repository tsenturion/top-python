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

switch x := 1; x {
case 1:
    fmt.Println("Один")
    fallthrouagh
case 2:
    fmt.Println("Два")
}

switch x := getValue(); {
case x > 10:
    fmt.Println("Больше десяти")
case x > 5:
    fmt.Println("Больше пяти")
default:
    fmt.Println("Пять или меньше")
}

if (x > 0) { // ❌ Ошибка

if x > 0 { // ✅ Правильно

if x > 0
    fmt.Println("Да") // ❌

if x := getValue(); x > 10 {
    fmt.Println(x)
}

// Здесь x больше не существует ❌

switch x {
case 1:
    fmt.Println("Один")
    fallthrough
case 2:
    fmt.Println("Два")
}

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

for i := 1; i <= 10; {
    fmt.Println(i) // ❌ i не увеличивается
}
for i := 1; i > 10; i++ {
    fmt.Println(i)
}




for i := 0; i < 3; i++ {
    fmt.Println(i)
}

fmt.Println(i) // ❌ ошибка — i не существует вне цикла


var age int
fmt.Scan(&age)

package main // Объявляем основной пакет программы

import (
    "fmt" // Импортируем пакет fmt для ввода/вывода
)

func main() {
    var age int // Объявляем переменную age типа int (целое число)

    fmt.Print("Введите ваш возраст: ") // Выводим приглашение ко вводу

    fmt.Scan(&age) // Считываем введённое пользователем число и сохраняем в переменную age

    // Начинаем конструкцию if-else для проверки возраста
    if age < 18 { // Если возраст меньше 18
        fmt.Println("Вы несовершеннолетний.") // Выводим соответствующее сообщение
    } else if age < 65 { // Иначе, если возраст меньше 65
        fmt.Println("Вы совершеннолетний.") // Выводим сообщение о совершеннолетии
    } else { // Во всех остальных случаях (то есть от 65 и выше)
        fmt.Println("Вы пенсионер.") // Сообщаем, что человек пенсионер
    }
}

package main // Основной пакет программы

import (
    "fmt" // Импортируем пакет fmt для ввода и вывода
)

func main() {
    var n int // Объявляем переменную n типа int

    fmt.Print("Введите положительное целое число: ") // Просим пользователя ввести число

    fmt.Scan(&n) // Считываем значение n с клавиатуры

    sum := 0 // Объявляем переменную sum и инициализируем её нулём — в ней будет храниться сумма

    // Цикл от 1 до n включительно
    for i := 1; i <= n; i++ {
        sum += i // На каждой итерации добавляем i к текущему значению sum
        // Например, при i = 1 → sum = 0 + 1
        // затем i = 2 → sum = 1 + 2 и т.д.
    }

    // После завершения цикла выводим итоговую сумму
    fmt.Printf("Сумма чисел от 1 до %d равна %d\n", n, sum)
}

if условие {
    // действия, если условие истинно
} else if другое_условие {
    // действия, если второе условие истинно
} else {
    // действия, если ни одно из условий не выполнено
}

package main

import "fmt"

func main() {
    age := 18

    if age >= 18 {
        fmt.Println("Доступ разрешён")
    }
}

package main

import "fmt"

func main() {
    temperature := 12

    if temperature < 10 {
        fmt.Println("Холодно")
    } else {
        fmt.Println("Тепло")
    }
}


package main

import "fmt"

func main() {
    score := 75

    if score >= 90 {
        fmt.Println("Оценка: A")
    } else if score >= 75 {
        fmt.Println("Оценка: B")
    } else if score >= 60 {
        fmt.Println("Оценка: C")
    } else {
        fmt.Println("Оценка: F")
    }
}

package main

import "fmt"

func main() {
    if x := 5; x%2 == 0 {
        fmt.Println("Чётное число")
    } else {
        fmt.Println("Нечётное число")
    }
}


package main

import "fmt"

func main() {
    day := "суббота"

    switch day {
    case "суббота", "воскресенье":
        fmt.Println("Выходной") // если день — суббота или воскресенье
    default:
        fmt.Println("Будний день") // для всех остальных дней
    }
}


package main

import "fmt"

func main() {
    grade := 3

    switch grade {
    case 5:
        fmt.Println("Отлично")
    case 4:
        fmt.Println("Хорошо")
    case 3:
        fmt.Println("Удовлетворительно")
    default:
        fmt.Println("Неудовлетворительно")
    }
}


package main

import "fmt"

func main() {
    score := 82

    switch {
    case score >= 90:
        fmt.Println("Оценка: A")
    case score >= 75:
        fmt.Println("Оценка: B")
    case score >= 60:
        fmt.Println("Оценка: C")
    default:
        fmt.Println("Оценка: F")
    }
}


package main

import "fmt"

func main() {
    temp := -5

    switch {
    case temp < 0:
        fmt.Println("Мороз") // температура ниже нуля
    case temp >= 0 && temp < 20:
        fmt.Println("Прохладно") // от 0 до 19
    default:
        fmt.Println("Тепло") // всё остальное (20 и выше)
    }
}

package main

import "fmt"

func main() {
    temp := -5

    switch {
    case temp < 0:
        fmt.Println("Мороз") // температура ниже нуля
    case temp >= 0 && temp < 20:
        fmt.Println("Прохладно") // от 0 до 19
    default:
        fmt.Println("Тепло") // всё остальное (20 и выше)
    }
}


package main

import "fmt"

func main() {
    x := 0

    for x < 5 { // пока x меньше 5
        fmt.Println(x) // выводим значение
        x++            // увеличиваем x на 1
    }
}

package main

import "fmt"

func main() {
    for i := 0; i < 5; i++ { // начинаем с i = 0, пока i < 5, увеличиваем i на 1
        fmt.Println(i) // выводим i на каждой итерации
    }
}


package main

import "fmt"

func main() {
    counter := 0

    for { // бесконечный цикл
        fmt.Println("Цикл номер", counter)
        counter++

        if counter == 3 { // условие выхода
            break // выход из цикла
        }
    }
}


switch {
case x > 10:
    // ...
case x > 5:
    // ...
}


for i := 0; i < 10; i++ {
    // обычный цикл
}

for condition {
    // как while
}

for {
    // бесконечный цикл
}

for ; i < 10; {
    // цикл без инициализации и пост-выражения
}

i := 0
for i < 5 {
    fmt.Println(i)
    // забыли i++
}

x := 10
if x > 5 {
    fmt.Println("A")
} else if x > 2 {
    fmt.Println("B")
} else {
    fmt.Println("C")
}

if n := 5; n < 10 {
    fmt.Println("Less than 10")
}
fmt.Println(n)

score := 75
switch {
case score >= 90:
    fmt.Println("A")
case score >= 70:
    fmt.Println("B")
default:
    fmt.Println("C")
}

i := 0
for i < 5 {
    fmt.Println(i)
}

for i := 1; i <= 5; i++ {
    fmt.Println(i)
}

for {
    fmt.Println("Ping")
}

x := 10
y := 5
if x > y {
    fmt.Println("A")
} else if x == y {
    fmt.Println("B")
} else {
    fmt.Println("C")
}

x := 10
for x < 20 {
    fmt.Println(x)
}

x := 10
switch x {
case 5:
    fmt.Println("Five")
case 10:
    fmt.Println("Ten")
default:
    fmt.Println("Other")
}

x := 7
if x > 5 && x < 10 {
    fmt.Println("In range")
} else {
    fmt.Println("Out of range")
}

for i := 0; i < 10; {
    fmt.Println(i)
}

x := 3
switch {
case x > 5:
    fmt.Println("Greater")
case x == 3:
    fmt.Println("Equal to 3")
default:
    fmt.Println("Other")
}

x := 15
if x < 10 {
    fmt.Println("Less")
} else if x > 10 {
    fmt.Println("Greater")
}


if x > 10 
{
	fmt.Println("x is greater than 10")
}



x := 10
if x = 10 {
	fmt.Println("x is ten")
}


switch day {
case "Monday":
	fmt.Println("Start of the week")
case "Friday":
	fmt.Println("End of the week")
}


for i := 1; i < 10; i++ {
	if i == 4 {
		break
	}
	fmt.Print(i)
}



package main

import "fmt"

func main() {
    // Инициализация переменной для ввода
    var age int

    // Цикл для 5 пользователей
    for i := 0; i < 5; i++ {
        // Запрос возраста у пользователя
        fmt.Print("Введите возраст: ")
        fmt.Scan(&age)

        // Определение статуса в зависимости от возраста
        if age < 18 {
            fmt.Println("Ребёнок")
        } else if age >= 18 && age <= 65 {
            fmt.Println("Взрослый")
        } else {
            fmt.Println("Пенсионер")
        }
    }
}

type ИмяСтруктуры struct {
    ИмяПоля1 ТипПоля1
    ИмяПоля2 ТипПоля2
    ...
}

type User struct {
    Name  string
    Email string
    Age   int
}

type Book struct {
    Title     string
    Author    string
    ISBN      string
    PageCount int
}

var u User

type Config struct {
    Port     int    // экспортируемое поле
    logLevel string // неэкспортируемое поле
}

// User представляет зарегистрированного пользователя системы.
type User struct {
    Name  string // Полное имя
    Email string // Адрес электронной почты
    Age   int    // Возраст
}

type Event struct {
    ID        int
    Name      string
    Handler   func()
    IsActive  bool
}

type Empty struct{}

flags := map[string]struct{}{}
flags["ready"] = struct{}{}

// В Go так делать нельзя:
type Bad struct {
    A, B, C int // Это ошибка
}

type Product struct {
    ID    int     // Уникальный идентификатор товара
    Name  string  // Название товара
    Price float64 // Цена
}

type User struct {
    Name string
    Age  int
}

var u User
u.Name = "Иван"
u.Age = 30

fmt.Println(u.Name) // Выведет: Иван
fmt.Println(u.Age)  // Выведет: 30

fmt.Println(getUser().Name)


type Point struct {
    X int
    Y int
}

p := Point{10, 20}
fmt.Println(p.X) // 10
fmt.Println(p.Y) // 20

p := Point{
    Y: 20,
    X: 10,
}


var u User
fmt.Println(u.Name) // пустая строка ""
fmt.Println(u.Age)  // 0


u := new(User) // *User
u.Name = "Анна"
fmt.Println(u.Name) // Анна


type Product struct {
    Name  string
    Price float64
}

func main() {
    var p Product
    p.Name = "Ноутбук"
    p.Price = 54999.90

    fmt.Println(p.Name)  // Ноутбук
    fmt.Println(p.Price) // 54999.9

    // Изменим цену:
    p.Price = 49999.90
    fmt.Println(p.Price) // 49999.9
}




type Employee struct {
    FirstName string
    LastName  string
    Position  string
    Salary    float64
}

func main() {
    e := Employee{
        FirstName: "Олег",
        LastName:  "Иванов",
        Position:  "Разработчик",
        Salary:    85000.0,
    }

    fmt.Println(e.FirstName, e.LastName) // Олег Иванов
    fmt.Println(e.Position)              // Разработчик

    // Повышение зарплаты
    e.Salary += 5000.0
    fmt.Println("Новая зарплата:", e.Salary) // 90000.0
}



type Car struct {
    Brand string
    Year  int
}

func main() {
    car := &Car{
        Brand: "Toyota",
        Year:  2021,
    }

    fmt.Println(car.Brand) // Toyota

    // Обновим год выпуска
    car.Year = 2022
    fmt.Println(car.Year) // 2022
}


func NewUser(name string, age int) User {
    return User{
        Name: name,
        Age:  age,
    }
}


type User struct {
    Name string
    Age  int
}

func updateAge(u User) {
    u.Age = u.Age + 1
    fmt.Println("Внутри функции:", u.Age)
}

func main() {
    user := User{Name: "Анна", Age: 30}
    updateAge(user)
    fmt.Println("Снаружи функции:", user.Age)
}



func updateAgePtr(u *User) {
    u.Age = u.Age + 1
    fmt.Println("Внутри функции:", u.Age)
}

func main() {
    user := User{Name: "Анна", Age: 30}
    updateAgePtr(&user)
    fmt.Println("Снаружи функции:", user.Age)
}


type Product struct {
    Name  string
    Price float64
}

func printProduct(p Product) {
    fmt.Println("Товар:", p.Name, "Цена:", p.Price)
}

func main() {
    pr := Product{"Ноутбук", 59990.0}
    printProduct(pr)
}


func applyDiscount(p *Product, discount float64) {
    p.Price = p.Price * (1 - discount)
}

func main() {
    pr := Product{"Телевизор", 89990.0}
    applyDiscount(&pr, 0.1) // скидка 10%
    fmt.Println("После скидки:", pr.Price)
}


func newUser(name string, age int) User {
    return User{Name: name, Age: age}
}

func main() {
    u := newUser("Алексей", 28)
    fmt.Println(u.Name, u.Age)
}


func newUserPtr(name string, age int) *User {
    return &User{Name: name, Age: age}
}

func main() {
    u := newUserPtr("Ольга", 35)
    fmt.Println(u.Name, u.Age)
}


type Address struct {
    City    string
    ZipCode string
}

type User struct {
    Name    string
    Age     int
    Address Address
}


type ContactInfo struct {
    Email string
    Phone string
}

type Employee struct {
    Name        string
    Department  string
    Contact     ContactInfo
}


type Person struct {
    Name string
    Age  int
}

type Employee struct {
    Person     // анонимное встраивание
    Position   string
    Department string
}


type Address struct {
    City    string
    ZipCode string
}

type User struct {
    Name    string
    Address Address
}
Объявим переменную:

user := User{
    Name: "Ольга",
    Address: Address{
        City:    "Москва",
        ZipCode: "101000",
    },
}

fmt.Println(user.Address.City) // Выведет: Москва

user.Address.ZipCode = "105005"

user.Profile.Contact.Email




type Address struct {
    City    string
    Street  string
    ZipCode string
}

type User struct {
    Name    string
    Age     int
    Address Address
}

func main() {
    user := User{
        Name: "Андрей",
        Age:  27,
        Address: Address{
            City:    "Казань",
            Street:  "Улица Ленина",
            ZipCode: "420000",
        },
    }

    fmt.Println("Город:", user.Address.City)
    fmt.Println("Улица:", user.Address.Street)
}



type Position struct {
    Title string
    Level int
}

type Employee struct {
    Name     string
    Position Position
}

func promote(e *Employee) {
    e.Position.Level++
}

func main() {
    emp := Employee{
        Name: "Сергей",
        Position: Position{
            Title: "Инженер",
            Level: 1,
        },
    }

    promote(&emp)
    fmt.Println("Новый уровень:", emp.Position.Level) // 2
}



type ContactInfo struct {
    Email string
    Phone string
}

type Profile struct {
    Username    string
    ContactInfo ContactInfo
}

type Account struct {
    ID      int
    Profile Profile
}

func main() {
    acc := Account{
        ID: 1001,
        Profile: Profile{
            Username: "ivan_dev",
            ContactInfo: ContactInfo{
                Email: "ivan@example.com",
                Phone: "+79991234567",
            },
        },
    }

    fmt.Println("Email:", acc.Profile.ContactInfo.Email)
}


type User struct {
    Name string
}

func (u User) Greet() {
    fmt.Println("Привет,", u.Name)
}

user := User{Name: "Анна"}
user.Greet() // Привет, Анна


func (r TypeName) MethodName() {
    // тело метода
}


type Rectangle struct {
    Width  float64
    Height float64
}

// Метод, привязанный к Rectangle
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}


type Counter struct {
    Value int
}

// Метод с получателем-значением
func (c Counter) IncrementByValue() {
    c.Value++
}

// Метод с получателем-указателем
func (c *Counter) IncrementByPointer() {
    c.Value++
}



func main() {
    c := Counter{Value: 10}

    c.IncrementByValue()
    fmt.Println(c.Value) // 10 — значение не изменилось

    c.IncrementByPointer()
    fmt.Println(c.Value) // 11 — значение изменилось
}


type Rectangle struct {
    Width  float64
    Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func main() {
    rect := Rectangle{Width: 5, Height: 3}
    fmt.Println("Площадь:", rect.Area()) // 15
}


type User struct {
    Name string
    Age  int
}

func (u *User) SetAge(newAge int) {
    u.Age = newAge
}

func main() {
    user := User{Name: "Иван", Age: 25}
    user.SetAge(30)
    fmt.Println(user.Age) // 30
}



type BankAccount struct {
    Owner  string
    Balance float64
}

// Метод просмотра баланса
func (b BankAccount) GetBalance() float64 {
    return b.Balance
}

// Метод пополнения
func (b *BankAccount) Deposit(amount float64) {
    b.Balance += amount
}

// Метод списания
func (b *BankAccount) Withdraw(amount float64) bool {
    if amount > b.Balance {
        return false
    }
    b.Balance -= amount
    return true
}

func main() {
    account := BankAccount{Owner: "Мария", Balance: 1000}
    account.Deposit(500)
    success := account.Withdraw(300)

    fmt.Println("Баланс:", account.GetBalance()) // 1200
    fmt.Println("Списание прошло:", success)    // true
}


func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}
Функция:

func Area(r Rectangle) float64 {
    return r.Width * r.Height
}

var numbers [5]int // Объявляется массив из 5 элементов типа int

var numbers [5]int

var days [7]string // Объявляется массив из 7 строк

var numbers = [3]int{10, 20, 30}

var numbers = [...]int{5, 15, 25, 35}

var numbers = [5]int{1: 100, 3: 300}



var numbers = [3]int{10, 20, 30}

fmt.Println(numbers[0]) // Выводит: 10
fmt.Println(numbers[2]) // Выводит: 30


numbers[1] = 99 // Заменяем второй элемент (индекс 1) на 99

fmt.Println(numbers) // Выводит: [10 99 30]


fmt.Println(numbers[3]) // Ошибка: индекс выходит за границы (index out of range)


var numbers = [4]int{5, 10, 15, 20}

fmt.Println(len(numbers)) // Вывод: 4


var emptyArray [10]string

fmt.Println(len(emptyArray)) // Вывод: 10



var numbers = [4]int{10, 20, 30, 40}

for i := 0; i < len(numbers); i++ {
    fmt.Println("Индекс:", i, "Значение:", numbers[i])
}


var numbers = [4]int{10, 20, 30, 40}

for index, value := range numbers {
    fmt.Println("Индекс:", index, "Значение:", value)
}


for _, value := range numbers {
    fmt.Println("Значение:", value)
}



var squares [5]int // Создаём массив из 5 целых чисел

for i := 0; i < len(squares); i++ {
    squares[i] = (i + 1) * (i + 1) // Записываем квадрат числа (индекс + 1)
}

fmt.Println(squares) // Вывод: [1 4 9 16 25]



var numbers = [5]int{3, 7, 1, 9, 5}
var target = 9
var found = false

for i := 0; i < len(numbers); i++ {
    if numbers[i] == target {
        fmt.Println("Найдено на позиции:", i)
        found = true
        break // Прерываем цикл после нахождения
    }
}

if !found {
    fmt.Println("Элемент не найден")
}



var original = [3]string{"Go", "Java", "Python"}
var copy [3]string // Массив такой же длины

for i := 0; i < len(original); i++ {
    copy[i] = original[i] // Копируем каждый элемент
}

fmt.Println("Исходный:", original)
fmt.Println("Копия   :", copy)




package main

import "fmt"

func modify(s []int) {
    s[0] = 999            // изменяем первый элемент
}

func main() {
    nums := []int{1, 2, 3}
    modify(nums)          // передаём срез в функцию

    fmt.Println(nums)     // [999 2 3]
}




package main

import "fmt"

func main() {
    arr := [5]int{1, 2, 3, 4, 5}
    s := arr[1:3]       // элементы 2, 3

    fmt.Println("len:", len(s)) // 2
    fmt.Println("cap:", cap(s)) // 4 (считает от s[0] до конца массива)
}




package main

import "fmt"

func main() {
    var a []int          // nil-срез
    b := []int{}         // пустой срез, не nil

    fmt.Println("a == nil:", a == nil) // true
    fmt.Println("b == nil:", b == nil) // false

    fmt.Println("len(a):", len(a))     // 0
    fmt.Println("len(b):", len(b))     // 0
}



package main

import "fmt"

func main() {
    base := []int{1, 2, 3}
    sub := base[:2]                 // создаём срез из первых двух элементов

    sub = append(sub, 100, 200)     // добавляем два элемента — может произойти переаллокация

    fmt.Println("base:", base)      // [1 2 3]
    fmt.Println("sub:", sub)        // [1 2 100 200]
}



package main

import "fmt"

func main() {
    arr := [5]int{1, 2, 3, 4, 5}   // обычный массив
    slice := arr[1:4]             // создаём срез с элементами 2, 3, 4

    slice[0] = 100                // меняем первый элемент среза (это arr[1])

    fmt.Println("Массив:", arr)   // [1 100 3 4 5]
    fmt.Println("Срез:", slice)   // [100 3 4]
}



package main

import "fmt"

func main() {
    numbers := []int{1, 2, 3, 4, 5, 6}   // исходный срез
    evens := []int{}                    // создаём пустой срез для чётных чисел

    for _, num := range numbers {       // обходим все элементы исходного среза
        if num%2 == 0 {                 // проверяем, делится ли число на 2 без остатка
            evens = append(evens, num)  // добавляем чётное число в новый срез
        }
    }

    fmt.Println("Чётные числа:", evens) // [2 4 6]
}



package main

import "fmt"

func main() {
    a := []int{1, 2, 3}          // создаём срез
    b := append(a, 4, 5)         // добавляем два элемента
    fmt.Println("b:", b)         // [1 2 3 4 5]

    c := make([]int, len(b))     // создаём новый срез нужной длины
    copy(c, b)                   // копируем элементы из b в c
    fmt.Println("c:", c)         // [1 2 3 4 5]
}



package main

import "fmt"

func main() {
    numbers := []int{1, 2, 3}  // создаём срез из трёх чисел

    numbers[0] = 10            // изменяем первый элемент
    numbers[2] = 30            // изменяем третий элемент

    fmt.Println(numbers)       // [10 2 30]
}


for _, value := range slice {
    fmt.Println(value)
}



package main

import "fmt"

func main() {
    slice := []string{"a", "b", "c"}

    for i, value := range slice {
        fmt.Println("Индекс:", i, "Значение:", value)
    }
}



package main

import "fmt"

func main() {
    src := []int{1, 2, 3}
    dst := make([]int, 3) // создаём срез-назначение нужной длины

    copied := copy(dst, src) // копируем src → dst
    fmt.Println("dst:", dst) // [1 2 3]
    fmt.Println("Скопировано элементов:", copied) // 3
}



package main

import "fmt"

func main() {
    nums := []int{10, 20, 30, 40, 50}
    part := nums[1:4] // берём элементы с индексами 1, 2, 3
    fmt.Println(part) // [20 30 40]
}


package main

import "fmt"

func main() {
    slice := make([]int, 2, 2) // длина и ёмкость 2
    fmt.Println("До append:", slice, "cap:", cap(slice))

    slice = append(slice, 100) // добавляем третий элемент → ёмкость будет увеличена
    fmt.Println("После append:", slice, "cap:", cap(slice))
}


package main

import "fmt"

func main() {
    slice := []int{1, 2, 3}         // создаём срез из трёх чисел
    slice = append(slice, 4, 5)     // добавляем два элемента
    fmt.Println(slice)              // [1 2 3 4 5]
}


package main

import "fmt"

func main() {
    slice := make([]int, 3, 5) // создаём срез длиной 3 и ёмкостью 5

    fmt.Println("Длина:", len(slice)) // 3
    fmt.Println("Ёмкость:", cap(slice)) // 5
}


package main

import "fmt"

func main() {
    slice := make([]int, 3, 5) // создаём срез из 3 элементов, ёмкостью 5
    fmt.Println(slice)         // [0 0 0]
}


package main

import "fmt"

func main() {
    slice := []string{"яблоко", "банан", "вишня"} // создаём срез строк
    fmt.Println(slice) // [яблоко банан вишня]
}


package main

import "fmt"

func main() {
    arr := [5]int{10, 20, 30, 40, 50} // создаём массив из 5 элементов
    slice := arr[1:4]                 // создаём срез с элементами от индекса 1 до 3 (не включая 4)

    fmt.Println(slice) // [20 30 40]
}


package main

import "fmt"

// Объявляем интерфейс
type Speaker interface {
    Speak()
}

// Объявляем структуру
type Dog struct{}

// Реализуем метод Speak для Dog
func (d Dog) Speak() {
    fmt.Println("Гав-гав!")
}

func main() {
    var s Speaker     // переменная интерфейсного типа
    s = Dog{}         // присваиваем значение структуры

    s.Speak()         // вызов метода через интерфейс
}



type Person struct {
    Name string
    Age  int
}


type Mover interface {
    Move()
}



var s Speaker
s = Dog{}
s.Speak()   // "Гав-гав!"

s = Person{Name: "Иван"}
s.Speak()   // "Привет, меня зовут Иван!"



type Printer interface {
    Print()
}

func SendToPrint(p Printer) {
    p.Print()
}




type ИмяИнтерфейса interface {
    Метод1(параметры) возвращаемые_значения
    Метод2(параметры) возвращаемые_значения
}

type Speaker interface {
    Speak()
}



type Animal interface {
    Speak()
    Walk()
}




package main

import "fmt"

// Объявляем интерфейс
type Speaker interface {
    Speak()
}

// Объявляем структуру
type Human struct {
    Name string
}

// Реализуем метод Speak
func (h Human) Speak() {
    fmt.Println("Привет, меня зовут", h.Name)
}

func main() {
    var s Speaker       // переменная интерфейсного типа
    s = Human{"Анна"}   // присваиваем значение, реализующее интерфейс

    s.Speak()           // вызываем метод через интерфейс
}




type Dog struct {
    Name string
}

func (d Dog) Speak() {
    fmt.Println("Гав! Я", d.Name)
}



var s Speaker

s = Human{"Анна"}
s.Speak()    // Привет, меня зовут Анна

s = Dog{"Шарик"}
s.Speak()    // Гав! Я Шарик



type Animal interface {
    Speak()
    Walk()
}

type Cat struct {
    Name string
}

func (c Cat) Speak() {
    fmt.Println("Мяу! Я", c.Name)
}

func (c Cat) Walk() {
    fmt.Println(c.Name, "идёт гулять")
}


type Empty interface{}

var _ Speaker = Human{}


type Greeter interface {
    Greet()
}




type Person struct {
    Name string
}

func (p Person) Greet() {
    fmt.Println("Привет! Меня зовут", p.Name)
}

type Dog struct {
    Name string
}

func (d Dog) Greet() {
    fmt.Println("Гав-гав! Я", d.Name)
}

type Robot struct {
    Model string
}

func (r Robot) Greet() {
    fmt.Println("Здравствуйте. Модель", r.Model, "включена.")
}


func SayHello(g Greeter) {
    g.Greet()
}




func main() {
    p := Person{Name: "Анна"}
    d := Dog{Name: "Шарик"}
    r := Robot{Model: "XJ-9"}

    SayHello(p) // Привет! Меня зовут Анна
    SayHello(d) // Гав-гав! Я Шарик
    SayHello(r) // Здравствуйте. Модель XJ-9 включена.
}



type Transporter interface {
    Move(passenger string)
}



type Car struct {
    Brand string
}

func (c Car) Move(passenger string) {
    fmt.Printf("%s едет в машине %s\n", passenger, c.Brand)
}

type Bicycle struct {
    Color string
}

func (b Bicycle) Move(passenger string) {
    fmt.Printf("%s едет на велосипеде цвета %s\n", passenger, b.Color)
}



func StartRide(t Transporter, name string) {
    t.Move(name)
}



func main() {
    car := Car{Brand: "Toyota"}
    bike := Bicycle{Color: "красный"}

    StartRide(car, "Олег")
    StartRide(bike, "Ирина")
}



func main() {
    p := Person{Name: "Алексей"}
    d := Dog{Name: "Бим"}
    r := Robot{Model: "RX-78"}

    greeters := []Greeter{p, d, r}

    for _, g := range greeters {
        g.Greet()
    }
}



func Describe(g Greeter) {
    switch v := g.(type) {
    case Person:
        fmt.Println("Это человек по имени", v.Name)
    case Dog:
        fmt.Println("Это собака по кличке", v.Name)
    case Robot:
        fmt.Println("Это робот модели", v.Model)
    default:
        fmt.Println("Неизвестный тип")
    }
}


interface{}


func PrintAnything(v interface{}) {
    fmt.Println("Значение:", v)
}


func main() {
    PrintAnything(42)
    PrintAnything("текст")
    PrintAnything(true)
    PrintAnything([]int{1, 2, 3})
}



func main() {
    var x interface{} = "Привет"

    s, ok := x.(string)
    if ok {
        fmt.Println("Строка:", s)
    } else {
        fmt.Println("Не строка")
    }
}



type error interface {
    Error() string
}



func Divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("деление на ноль недопустимо")
    }
    return a / b, nil
}



func main() {
    result, err := Divide(10, 0)
    if err != nil {
        fmt.Println("Ошибка:", err)
        return
    }
    fmt.Println("Результат:", result)
}


type MyError struct {
    Code int
    Msg  string
}

func (e MyError) Error() string {
    return fmt.Sprintf("Код ошибки %d: %s", e.Code, e.Msg)
}


func DoSomething() error {
    return MyError{Code: 123, Msg: "Что-то пошло не так"}
}


func main() {
    err := DoSomething()
    if err != nil {
        fmt.Println("Ошибка:", err)
    }
}




type SuperService interface {
    Save()
    Load()
    Delete()
    Export()
    Import()
    Validate()
    Print()
}



type Saver interface {
    Save()
}

type Loader interface {
    Load()
}

type Validator interface {
    Validate()
}



type User struct {
    ID   interface{}
    Name interface{}
    Age  interface{}
}




type User struct {
    ID   int
    Name string
    Age  int
}



type FileService struct {}

func (fs FileService) Save(path string, data []byte) error {
    // сохранение в файл
    return nil
}



type Saver interface {
    Save(path string, data []byte) error
}




type FileService struct {}

func (fs FileService) Save(...) error { ... }



type Storage interface {
    Save(path string, data []byte) error
}









package main

import (
    "fmt"
    "math"
)

// 1. Объявляем интерфейс Shape
type Shape interface {
    // Метод, возвращающий площадь фигуры
    Area() float64
}

// 2. Объявляем структуру Rectangle
type Rectangle struct {
    Width, Height float64
}

// 2. Объявляем структуру Circle
type Circle struct {
    Radius float64
}

// 3. Реализация метода Area для Rectangle
func (r Rectangle) Area() float64 {
    // Площадь прямоугольника = ширина * высота
    return r.Width * r.Height
}

// 3. Реализация метода Area для Circle
func (c Circle) Area() float64 {
    // Площадь круга = π * r²
    return math.Pi * c.Radius * c.Radius
}

// 4. Функция суммирует площади всех фигур из среза
func TotalArea(shapes []Shape) float64 {
    var total float64
    for _, s := range shapes {
        // Для каждого элемента вызываем метод Area()
        total += s.Area()
    }
    return total
}

func main() {
    // Создаём несколько фигур
    rect1 := Rectangle{Width: 3, Height: 4}
    rect2 := Rectangle{Width: 5, Height: 2}
    circle1 := Circle{Radius: 2.5}

    // Собираем их в срез интерфейсного типа
    shapes := []Shape{rect1, rect2, circle1}

    // Вычисляем и выводим суммарную площадь
    fmt.Printf("Суммарная площадь: %.2f\n", TotalArea(shapes))
}










package main

import "fmt"

// 1. Объявляем интерфейс Notifier
type Notifier interface {
    // Метод отправки уведомления
    Notify(message string)
}

// 2. Объявляем EmailNotifier
type EmailNotifier struct {
    EmailAddress string
}

// 2. Объявляем SMSNotifier
type SMSNotifier struct {
    PhoneNumber string
}

// 3. Реализация Notify для EmailNotifier
func (e EmailNotifier) Notify(message string) {
    // В реальном приложении здесь был бы SMTP-сервер
    fmt.Printf("Email to %s: %s\n", e.EmailAddress, message)
}

// 3. Реализация Notify для SMSNotifier
func (s SMSNotifier) Notify(message string) {
    // Здесь мог бы быть вызов SMS-шлюза
    fmt.Printf("SMS to %s: %s\n", s.PhoneNumber, message)
}

// 4. Универсальная функция для рассылки уведомлений
func SendNotifications(nots []Notifier, msg string) {
    for _, n := range nots {
        // Для каждого Notifier вызываем Notify
        n.Notify(msg)
    }
}

func main() {
    // 5. Создаём конкретные Notifier
    email := EmailNotifier{EmailAddress: "user@example.com"}
    sms := SMSNotifier{PhoneNumber: "+71234567890"}

    // Собираем их в срез интерфейсного типа
    notifiers := []Notifier{email, sms}

    // Тестовое сообщение
    message := "Ваш отчёт готов!"

    // Отправляем всем сразу
    SendNotifications(notifiers, message)
}



package main

import (
    "fmt"
    "uuidlib" // воображаемая внешняя библиотека
)

func main() {
    id := uuidlib.Generate()
    fmt.Println("Сгенерированный UUID:", id)
}


package main

import "fmt"

func main() {
    fmt.Println("Привет, Go!")
}


import "example.org/somepkg"


package main

import (
    "fmt"
    "example.org/somepkg"
)

func main() {
    result := somepkg.DoSomething()
    fmt.Println(result)
}
