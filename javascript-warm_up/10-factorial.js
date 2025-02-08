#!/usr/bin/node

function factorial (n) {
  // Convert argument to integer
  const num = parseInt(n);

  // Handle NaN case
  if (isNaN(num)) {
    return 1;
  }

  // Base cases
  if (num <= 0) {
    return 1;
  }

  // Recursive case
  return num * factorial(num - 1);
}

// Get first argument from command line
const arg = process.argv[2];
console.log(factorial(arg));
