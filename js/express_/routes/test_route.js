const express = require('express')
const router = express.Router()
const test_controller = require('../controllers/test_controller.js')



router.get('/', test_controller.main)

router.get('/about', test_controller.about)


module.exports = router
