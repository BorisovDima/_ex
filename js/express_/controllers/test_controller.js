
function main(req, res){
  res.send('Home')
}
function about(req, res){
  res.send('About')
  res.append('Set-Cookie', 'foo=bar; Path=/; HttpOnly');
}


module.exports = {
  about,
  main
}
