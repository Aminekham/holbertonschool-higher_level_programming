#!/usr/bin/node

exports.esrever = function (list){
  l = [];
  for (let i = list.length; i >= 0; i--){
    l.psuh(list[i]);
  }
  return(l);
}