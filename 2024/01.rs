use std::fs::File;
use std::io::{BufRead, BufReader, Result};

fn read_and_parse(filename: &str) -> Result<(Vec<i32>, Vec<i32>)> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut ileft: Vec<i32> = Vec::new();
    let mut iright: Vec<i32> = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split("   ").collect();

        if parts.len() == 2 {
            if let (Ok(l_el), Ok(r_el)) = (parts[0].parse::<i32>(), parts[1].parse::<i32>()) {
                ileft.push(l_el);
                iright.push(r_el);
            }
        }
    }

    Ok((ileft, iright))
}

fn remove_min(nums: &mut Vec<i32>) -> Option<i32> {
    if nums.is_empty() {
        return None;
    }

    let min_index = nums
        .iter()
        .enumerate()
        .min_by_key(|&(_, value)| value)
        .map(|(index, _)| index)
        .unwrap();

    Some(nums.remove(min_index))
}

fn main() -> std::io::Result<()> {
    let (ileft, iright) = read_and_parse("01.txt")?;

    let mut left = ileft;
    let mut right = iright;

    let mut dists: Vec<i32> = Vec::new();
    for _ in 0..left.len() {
        let lmin: i32 = remove_min(&mut left).unwrap_or(0);
        let rmin: i32 = remove_min(&mut right).unwrap_or(0);
        dists.push((lmin-rmin).abs());
    }
    let sum: i32 = dists.iter().sum();
    println!("sum distances: {}", sum);

    Ok(())
}
