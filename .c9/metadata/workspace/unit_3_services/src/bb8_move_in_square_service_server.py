{"filter":false,"title":"bb8_move_in_square_service_server.py","tooltip":"/unit_3_services/src/bb8_move_in_square_service_server.py","undoManager":{"mark":44,"position":44,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":40},"action":"insert","lines":["#! /usr/bin/env python","","import rospy","from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.","","","def my_callback(request):","    print \"My_callback has been called\"","    return EmptyResponse() # the service Response class, in this case EmptyResponse","    #return MyServiceResponse(len(request.words.split())) ","","rospy.init_node('service_server') ","my_service = rospy.Service('/my_service', Empty , my_callback) # create the Service called my_service with the defined callback","rospy.spin() # mantain the service open."],"id":1}],[{"start":{"row":12,"column":29},"end":{"row":12,"column":39},"action":"remove","lines":["my_service"],"id":2},{"start":{"row":12,"column":29},"end":{"row":12,"column":47},"action":"insert","lines":["move_bb8_in_square"]}],[{"start":{"row":11,"column":17},"end":{"row":11,"column":31},"action":"remove","lines":["service_server"],"id":3},{"start":{"row":11,"column":17},"end":{"row":11,"column":35},"action":"insert","lines":["move_bb8_in_square"]}],[{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"insert","lines":["_"],"id":4}],[{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"insert","lines":["s"],"id":5}],[{"start":{"row":11,"column":37},"end":{"row":11,"column":38},"action":"insert","lines":["r"],"id":6}],[{"start":{"row":11,"column":38},"end":{"row":11,"column":39},"action":"insert","lines":["v"],"id":7}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":22},"action":"remove","lines":["My_callback"],"id":8},{"start":{"row":7,"column":11},"end":{"row":7,"column":29},"action":"insert","lines":["move_bb8_in_square"]}],[{"start":{"row":2,"column":12},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["i"],"id":10}],[{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["m"],"id":11}],[{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["p"],"id":12}],[{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["o"],"id":13}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["r"],"id":14}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["t"],"id":15}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":[" "],"id":16}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["B"],"id":17}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["B"],"id":18}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":9},"action":"remove","lines":["BB"],"id":19},{"start":{"row":3,"column":7},"end":{"row":3,"column":11},"action":"insert","lines":["BB88"]}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":11},"action":"remove","lines":["BB88"],"id":20},{"start":{"row":3,"column":7},"end":{"row":3,"column":14},"action":"insert","lines":["MoveBB8"]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"],"id":21}],[{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"],"id":22}],[{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"],"id":23}],[{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"],"id":24}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":25}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["m"],"id":26}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["o"],"id":27}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["v"],"id":28}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["e"],"id":29}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["_"],"id":30}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["b"],"id":31}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["b"],"id":32}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":12},"action":"remove","lines":["move_bb"],"id":33},{"start":{"row":3,"column":5},"end":{"row":3,"column":13},"action":"insert","lines":["move_bb8"]}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":[" "],"id":34}],[{"start":{"row":8,"column":46},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":33},"action":"insert","lines":["moveBB =  MoveBB8('/cmd_vel')"],"id":36}],[{"start":{"row":9,"column":33},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["m"],"id":38}],[{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["o"],"id":39}],[{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["v"],"id":40}],[{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["e"],"id":41}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["B"],"id":42}],[{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["B"],"id":43}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["."],"id":44}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":23},"action":"insert","lines":["moveSquare()"],"id":45}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":40},"end":{"row":16,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1544529549234,"hash":"4f77cc011ff392d8db738e59a5b102c82a408474"}