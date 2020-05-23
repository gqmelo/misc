pub trait Summary {
    fn summarize(&self) -> String {
        format!("New item from {}", self.summarize_author())
    }
    fn summarize_author(&self) -> String;
}

#[derive(Debug)]
pub struct NewsArticle {
    pub title: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize_author(&self) -> String {
        format!("{}", self.author)
    }
}

#[derive(Debug)]
pub struct Tweet {
    pub username: String,
    pub content: String,
}

impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
