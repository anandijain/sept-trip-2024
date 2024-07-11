use reqwest::Error;
use serde::{Deserialize, Serialize};
use serde_json::Value;

// coast campground
// https://www.openstreetmap.org/way/233668396#map=17/38.01849/-122.85224
// its a way and we probably for distance calculation and graph search we cant just use the center point of the way (well i could to start)

// coast trail which intersects the campground way 
// https://www.openstreetmap.org/way/421882260#map=16/38.0197/-122.8610
// i want to get the position of the intersection of the coast trail and the campground way
// its likely that the nodes defining each of these ways wont have an intersection so a calculation needs to be done to find it


// const string literal
#[tokio::main]
async fn main() -> Result<(), Error> {
    // let point_reyes_id ="233359";
    let url = 
    let response = reqwest::get(url).await?.json::<Value>().await?;

    Ok(())
}
