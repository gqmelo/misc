use std::fs::File;

mod traits;
use traits::{NewsArticle, Summary, Tweet};

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

    let user3 = User {
        email: String::from("bar@foo.com"),
        username: String::from("anotherusername"),
        ..user2
    };
    println!("My struct: {:?}", user3);

    let color = Color(0, 0, 0);
    println!("My color: {:#?}", color);

    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    println!("Rectangle: {:?}", rect1);
    println!("Rectangle area: {}", rect1.area());

    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));

    let square1 = Rectangle::square(4);
    println!("Square: {:?}", square1);

    let message1 = Message::Quit;
    let message2 = Message::Move { x: 100, y: 90 };
    let message3 = Message::Write(String::from("something"));
    let message4 = Message::ChangeColor(255, 0, 255);

    println!("Message: {:?}", message1);
    println!("Message: {:?}", message2);
    println!("Message: {:?}", message3);
    println!("Message: {:?}", message4);

    if let Message::Move { x, y } = message2 {
        println!("Got a Move message: x: {}, y: {}", x, y);
    } else {
        println!("Not a Move message");
    }

    let some_number = Some(10);
    let absent_number: Option<u32> = None;

    fn process_optional_number(num: Option<u32>) {
        match num {
            Some(i) => println!("Got value {}", i),
            None => println!("Got no value"),
        };
    }

    process_optional_number(some_number);
    process_optional_number(absent_number);

    // Modules
    sound::instrument::clarinet();
    crate::sound::instrument::clarinet();

    let mut v1: Vec<i32> = Vec::new();
    v1.push(1);
    v1.push(110);
    println!("v={:?}", v1);

    let v2 = vec![4, 32, 1];
    println!("v={:?}", v2);

    println!("Third elem: {}", v2[2]);
    // Causes panic
    // println!("100th elem: {}", v2[99]);
    match v1.get(2) {
        Some(third) => println!("Third elem: {}", third),
        None => println!("No third elem found"),
    }

    let first_elem = &v1[0];
    // Causes error dur to immutable borrow
    // v1.push(10);
    println!("First elem: {}", first_elem);

    for i in &v1 {
        println!("elem: {}", i);
    }
    for i in &mut v1 {
        *i += 1;
        println!("elem: {}", i);
    }
    println!("v={:?}", v1);

    // Storing different types in an Array
    #[derive(Debug)]
    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }
    let row = vec![
        SpreadsheetCell::Int(10),
        SpreadsheetCell::Text(String::from("Text")),
        SpreadsheetCell::Float(20.345),
    ];
    println!("Row: {:?}", row);

    // Strings
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let concat_str1 = s1 + &s2 + &s3;
    // doesn't work, s1 was moved
    // let concat_str2  = s1 + &s2 + &s3;
    let concat_str2 = s2 + &s3;

    println!("{}", concat_str1);
    println!("{}", concat_str2);

    let hello = "Здравствуйте";
    println!("utf8_length={}", hello.len());

    let hello = "Здравствуйте";
    println!("slice={}", &hello[0..4]);
    // This panics as we are not getting the whole char
    // println!("slice={}", &hello[0..1]);

    // Hash maps
    use std::collections::HashMap;

    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    println!("scores={:#?}", scores);

    // Creating a HashMap from lists using zip
    let teams = vec![String::from("Blue"), String::from("Yellow")];
    let initial_scores = vec![10, 50];
    let mut scores: HashMap<_, _> = teams.iter().zip(initial_scores.iter()).collect();
    println!("scores={:#?}", scores);

    let team = String::from("Purple");
    scores.insert(&team, &29);
    println!("Team name: {}", team);
    let mut scores = HashMap::new();
    scores.insert(team, 29);
    // Can't use team again as it was borrowed by HashMap
    // println!("Team name: {}", team);
    println!("Purple: {:#?}", scores.get(&String::from("Purple")));
    println!("Red: {:#?}", scores.get(&String::from("Red")));

    // Default values
    scores.entry(String::from("Red")).or_default();
    scores.entry(String::from("Blue")).or_insert(99);
    println!("Red: {:#?}", scores.get(&String::from("Red")));
    println!("Blue: {:#?}", scores.get(&String::from("Blue")));
    let score = scores.entry(String::from("Green")).or_insert(99);
    *score += 1;
    println!("Green: {:#?}", scores.get(&String::from("Green")));

    // panic!("Everything is on fire!!!");
    let v = vec![1, 2, 3];
    // v[100];

    // Error handling (Result)
    use std::io::ErrorKind;
    let f = File::open("/tmp/hello.txt");
    let f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("/tmp/hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Could not create file {:?}", e),
            },
            other_error => panic!("Error opening file {:#?}", other_error),
        },
    };
    // Both cause a panic
    // let f2 = File::open("/tmp/hello2.txt").unwrap();
    // let f2 = File::open("/tmp/hello2.txt").expect("Something happened");

    let username = match read_username_from_file() {
        Ok(value) => value,
        Err(e) => {
            println!("Could not read username: {:?}", e);
            String::from("default_user")
        }
    };
    println!("username: {}", username);

    let username = match read_username_from_file_simplified() {
        Ok(value) => value,
        Err(e) => {
            println!("Could not read username: {:?}", e);
            String::from("default_user")
        }
    };
    println!("username: {}", username);

    let username = match read_username_from_file_even_more_simplified() {
        Ok(value) => value,
        Err(e) => {
            println!("Could not read username: {:?}", e);
            String::from("default_user")
        }
    };
    println!("username: {}", username);

    let point = Point { x: 3, y: 5 };
    // method is defined only for f32 type
    // point.distance_from_origin();
    println!("point int: {:?}", point);

    let point = Point { x: 2.0, y: 10.0 };
    println!(
        "point float: {:?}; distance from origin: {}",
        point,
        point.distance_from_origin()
    );

    // ################################################
    // Traits
    // ################################################
    let news = NewsArticle {
        title: String::from("Some news"),
        author: String::from("Me"),
        content: String::from("Some content"),
    };

    let tweet = Tweet {
        username: String::from("abc123"),
        content: String::from("Some tweet"),
    };

    println!("tweet: {:?}", tweet);
    println!("tweet summary: {:?}", tweet.summarize());
    println!("news: {:?}", news);
    println!("news summary: {:?}", news.summarize());
}

#[derive(Debug)]
enum Message {
    Quit,
    Move { x: u32, y: u32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

#[derive(Debug)]
struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

#[derive(Debug)]
struct Color(i32, i32, i32);

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, rectangle: &Rectangle) -> bool {
        self.width > rectangle.width && self.height > rectangle.height
    }

    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }
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

mod sound {
    pub mod instrument {
        pub fn clarinet() {
            super::breath_in();
        }
    }

    fn breath_in() {}
}

use std::io;
use std::io::Read;

fn read_username_from_file() -> Result<String, io::Error> {
    let f = File::open("hello.txt");

    let mut f = match f {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut s = String::new();
    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    }
}

fn read_username_from_file_simplified() -> Result<String, io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

use std::fs;
fn read_username_from_file_even_more_simplified() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}

#[derive(Debug)]
struct Point<T> {
    x: T,
    y: T,
}

// impl<T> Point<T> {
//     fn sum(&self) -> T {
//         self.x + self.y
//     }
// }

impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}

// fn largest<T>(list: &[T]) -> T {
//     let mut largest = list[0];
//     for &item in list {
//         if item > largest {
//             largest = item;
//         }
//     }

//     largest
// }
