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
    // let number = if condition {
    //     5
    // } else {
    //     "six"
    // };
    println!("Number is {}", number);

    let mut counter = 0;
    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
        // else {
        //     break 1;
        // }
    };
    println!("The result is {}", result);

    let a = [10, 20, 30, 40, 50];
    for element in a.iter() {
        println!("The element value is {}", element)
    }

    for number in (1..4).rev() {
        println!("{}!", number);
    }
    println!("LIFTOFF!!!");

    let mut s = String::from("hello");
    s.push_str(", world!");
    println!("{}", s);

    let s1 = String::from("hello");
    let s2 = s1;

    // Fails to compile with "borrow  of moved value: `s1`"
    // println!("{}, world!", s1);

    let s1 = String::from("hello");
    let s2 = s1.clone();
    println!("s1 = {}, s2 = {}", s1, s2);

    let s = String::from("hello");
    takes_ownership(s);
    let x = 5;
    makes_copy(x);
    // s already moved
    // let w = s;

    // References and borrowing

    let s1 = String::from("hello reference");
    let len = calculate_length(&s1); // This is borrowing
    println!("The length of '{}' is {}", s1, len);

    let mut s1 = String::from("hello reference");
    change(&mut s1);
    println!("Changed string: {}", s1);

    // let r1 = &mut s1;
    // Not allowed because variables can be borrowed only once as mutable
    // let r2 = &mut s1;
    // println!("r1: {}, r2: {}", r1, r2);

    {
        let r1 = &mut s1;
    }
    let r2 = &mut s1;
    println!("r2: {}", r2);

    let r1 = &s1;
    let r2 = &s1;
    // Can't borrow as mutable while it also borrowed as imutable
    // let r3 = &mut s1;
    println!("r1: {}, r2: {}", r1, r2);

    // Slices

    let s = String::from("hello world");
    let hello = &s[..5];
    let world = &s[6..11];
    println!("slice1: {}, slice2: {}", hello, world);

    let s = String::from("hello world");
    // let mut s = String::from("hello world");
    let word = first_word(&s);
    // clear causes a mutable borrow conflicting with the immutable one (slice)
    // s.clear();
    println!("First word: {}", word);
    println!("Second word: {}", first_word(&s[6..]));

    let a = [1, 2, 3, 4, 5];
    let slice = &a[..3];
    // {:?} uses the Debug trait: https://doc.rust-lang.org/std/fmt/trait.Debug.html
    println!("Array slice: {:?}", slice);

    let user1 = User {
        email: String::from("foo@bar.com"),
        username: String::from("someusername"),
        active: false,
        sign_in_count: 10,
    };
    println!("My struct: {:?}", user1);
    println!("Username: {}", user1.username);

    // user1 is immutable
    // user1.username = String::from("Another name");

    let mut user2 = User {
        email: String::from("foo@bar.com"),
        username: String::from("someusername"),
        active: false,
        sign_in_count: 10,
    };
    user2.username = String::from("Another name");
    println!("My struct: {:?}", user2);
}

#[derive(Debug)]
struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

fn takes_ownership(some_string: String) {
    println!("some_string = {}", some_string);
}

fn makes_copy(some_integer: u32) {
    println!("some_integer = {}", some_integer);
}

fn another_function(x: i32, y: i64) {
    println!("The value of x is: {}", x);
    println!("The value of y is: {}", y);
}

fn five() -> i32 {
    5
}

fn calculate_length(s: &String) -> usize {
    s.len()
}

fn change(some_string: &mut String) {
    some_string.push_str(" something");
}

// fn first_word(s: &String) -> &str {
// This lets literals to be passed. str is a slice and literals are slices.
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[..i];
        }
    }

    &s[..]
}