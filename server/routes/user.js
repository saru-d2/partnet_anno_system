var express = require('express');
var router = express.Router();
var request = require('request');
var server = require('../config/server.js');

const mysql = require('mysql2');

const pool = mysql.createPool({
    host: server.DB_HOST,
    user: server.DB_USER,
    password: server.DB_PASSWORD,
    database: server.DB_NAME,
});
console.log('haha');
router.post('/login', function(req, res) {
    const username = req.body.username;
    const password = req.body.password;

    let login_success = false;
    // console.log('server details :'+str(server.DB_HOST)+' '+str(server.DB_USER)+' '+str(server.DB_PASSWORD)+' '+str(server.DB_NAME));

    // Find in mysql database to check for the credentials
    pool.getConnection(function (error, connection) {
        // if (error) throw error;
        if (error) {
            console.log('[ connect error ]');
            // console.log('server details :'+str(server.DB_HOST)+' '+str(server.DB_USER)+' '+str(server.DB_PASSWORD)+' '+str(server.DB_NAME));
            login_success = false;
        } else {
            console.log("[ database connected ]");
        }
        // console.log(connection, typeof(connnection));
        console.log(typeof(connection));
        const query = "SELECT password\n" +
            "FROM Worker\n" +
            "WHERE workerID = '" + username +
            "';";
        connection.query(query, function (error, results, field) {
            if (error) {
                console.log('[ error (threw) ]', error);
                // throw error;
                login_success = false;
                return;
            }
            console.log('[ result ]', results[0]);  // the variables can be accessed by 'results[0].<variable name from 'AS'>'
            if (results[0] === undefined) {
                login_success = false;
            }
            else if (results[0].password === password) {
                login_success = true;
            }
            console.log('login_success:', login_success);
            if (login_success) {
                const url = server.HOST + ':' + server.PORT + '/part_anno_list_viewer';
                res.redirect(307, '/part_anno_list_viewer');
                // res.redirect(307, url);
            } else {
                res.render('index', {
                    title: 'PartNet Annotation Server',
                    login_alert_txt: 'The credentials are not correct!',
                    signup_alert_txt: ''
                });
            }

            connection.release();
        });
    });
});


router.post('/signup', function(req, res) {
    const username = req.body.username;
    const password = req.body.password;
    const realname = req.body.realname;
    const email = req.body.email;
    const ip = req.connection.remoteAddress;

    let sign_success = false;

    // create a new user in the database
    pool.getConnection(function (error, connection) {
        if (error) {
            console.log('[ connect error ]');
            console.log(error+' ');
            console.log('server details:'+String(server.DB_HOST)+' '+String(server.DB_USER)+' '+String(server.DB_PASSWORD)+' '+String(server.DB_NAME));

            sign_success = false;
        } else {
            console.log("[ database connected ]");
        }
        const query = "INSERT INTO Worker (workerID, password, realname, email, ip) VALUES ('" + username +
            "', '" + password +
            "', '" + realname +
            "', '" + email +
            "', '" + ip +
            "');";
        connection.query(query, function (error, results, field) {
            if (error) {
                console.log('[ error ]', error);
                res.render('index', {
                    title: 'PartNet Annotation Server',
                    signup_alert_txt: 'Username has been used! Please choose a new one!',
                    login_alert_txt: ''
                });
                connection.release();
            } else {
                res.render('index', {
                    title: 'PartNet Annotation Server',
                    signup_alert_txt: 'Successfully create a new user in database! Please login!',
                    login_alert_txt: ''
                });
                connection.release();
            }
        });

    });
});

module.exports = router;

