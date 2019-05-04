fn main() {
    println!("Hello, world!");
    another_function(5, 6);

    let a = {
        let x = 10;
        x + 1
    };
    println!("The value of a is {}", a);
    println!("The value of five is {}", five());

    let condition = true;
    let number = if condition { 5 } else { 6 };
    let number = if condition { 5 } else { "six" };
    println!("Number is {}", number);
}

fn another_function(x: i32, y: i64) {
    println!("The value of x is: {}", x);
    println!("The value of y is: {}", y);
}

fn five() -> i32 {
    5
}
