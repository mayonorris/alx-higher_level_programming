#!/usr/bin/node
const { dict } = require('./101-data');
// Initialize an empty object to store the result
const result = {};
// Iterate over the keys (user ids) and values (occurrences) in the original dictionary
Object.keys(dict).forEach(userId => {
  const occurrences = dict[userId];
  // If the occurrences key does not exist in the result object, initialize it with an empty array
  if (!result[occurrences]) {
    result[occurrences] = [];
  }
  // Push the userId into the corresponding occurrences key in the result object
  result[occurrences].push(userId);
});
console.log(result);
