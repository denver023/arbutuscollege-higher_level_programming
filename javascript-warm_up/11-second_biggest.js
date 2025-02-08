#!/usr/bin/node

const args = process.argv.slice(2);

// If no arguments or only one argument, print 0
if (args.length <= 1) {
  console.log(0);
} else {
  // Convert all arguments to integers and remove duplicates
  const numbers = [...new Set(args.map(num => parseInt(num)))];

  // Sort in descending order
  numbers.sort((a, b) => b - a);

  // Print second element (second biggest)
  console.log(numbers[1]);
}
