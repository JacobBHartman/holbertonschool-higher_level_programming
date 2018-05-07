#!/usr/bin/node

exports.converter = function (base) {
  function convertIt (number) {
    return number.toString(base);
  }
  return convertIt;
};
