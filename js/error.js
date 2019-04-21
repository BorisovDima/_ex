let func = ()=>{
   try {
      throw new SyntaxError('BODY') // like raise
   }
   catch(err) {
      console.log(err.name, err.message)
   }
   finally{
     console.log('Finaly')
   }
}
func()
