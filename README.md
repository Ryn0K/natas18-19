# natas18-19
# overthewire.org
# ctfchallenges
The python script to automate task to find specific PHPSESSID for the website to retreive the password for next level.
After reading ,the source code given on this challenge website .
i concluded that the website uses the session_id to login as admin,
        i.e if($_COOKIE['PHPSESSID']==somenumber) and if (sessionid=somenumber){then $_SESSION['admin']=1}
        if $_SESSION['admin']==1
        then 
        function show the credential for next level

so we try bruteforce PHPSESSID 1 b/w 641 if somenumber is found then server responds with the bunch of credential for next level.


                                              --written by krn_bhargav
                                              For more info contact at
                                              insta@krn_bhargav
                                              kkbhargavmail@gmail.com
