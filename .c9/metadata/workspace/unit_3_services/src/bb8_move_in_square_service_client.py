{"filter":false,"title":"bb8_move_in_square_service_client.py","tooltip":"/unit_3_services/src/bb8_move_in_square_service_client.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["q"],"id":80}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["u"],"id":81}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":21},"action":"remove","lines":["requ"],"id":82},{"start":{"row":8,"column":17},"end":{"row":8,"column":24},"action":"insert","lines":["request"]}],[{"start":{"row":8,"column":25},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":83}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":83},"action":"remove","lines":["rospy.init_node('unit_3_node') # Initialise a ROS node with the name service_client"],"id":84}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":85}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":86}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":83},"action":"insert","lines":["rospy.init_node('unit_3_node') # Initialise a ROS node with the name service_client"],"id":87}],[{"start":{"row":12,"column":0},"end":{"row":21,"column":0},"action":"remove","lines":["","","rospy.wait_for_service('/execute_trajectory') # Wait for the service client /gazebo/delete_model to be running","exec_traj = rospy.ServiceProxy('/execute_trajectory', ExecTraj) # Create the connection to the service","request = ExecTrajRequest()","request.file = traj","#kk.file = traj # Fill the variable model_name of this object with the desired value","result = exec_traj(request) # Send through the connection the name of the object to be deleted by the service","",""],"id":88}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":28},"action":"remove","lines":["unit_3_node"],"id":89},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["b"]}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["b"],"id":90}],[{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["8"],"id":91}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["_"],"id":92}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["c"],"id":93}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["l"],"id":94}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["i"],"id":95}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["i"],"id":96}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["l"],"id":97}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["c"],"id":98}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["m"],"id":99}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["o"],"id":100},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["p"]}],[{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["v"],"id":101}],[{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"remove","lines":["v"],"id":102}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["p"],"id":103}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["v"],"id":104}],[{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["e"],"id":105}],[{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["_"],"id":106}],[{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["c"],"id":107}],[{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["l"],"id":108}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["i"],"id":109}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["e"],"id":110}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["n"],"id":111}],[{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["t"],"id":112}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["p"],"id":113}],[{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["r"],"id":114}],[{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["i"],"id":115}],[{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["n"],"id":116}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["t"],"id":117}],[{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":[" "],"id":118}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":8},"action":"insert","lines":["()"],"id":119}],[{"start":{"row":5,"column":7},"end":{"row":5,"column":9},"action":"insert","lines":["''"],"id":120}],[{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["I"],"id":121}],[{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["n"],"id":122}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":[" "],"id":123}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["c"],"id":124}],[{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["l"],"id":125}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["i"],"id":126}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["e"],"id":127}],[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["n"],"id":128}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["t"],"id":129}],[{"start":{"row":10,"column":25},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":130}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":131}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["p"],"id":132}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":["r"],"id":133}],[{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"insert","lines":["i"],"id":134}],[{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"insert","lines":["n"],"id":135}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["t"],"id":136}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":[" "],"id":137}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["r"],"id":138}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["e"],"id":139}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["s"],"id":140}],[{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["u"],"id":141}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":10},"action":"remove","lines":["resu"],"id":142},{"start":{"row":12,"column":6},"end":{"row":12,"column":12},"action":"insert","lines":["result"]}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["\\"],"id":143}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["\\"],"id":144}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"remove","lines":["\\"],"id":145}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["/"],"id":146}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"remove","lines":["\\"],"id":147}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["/"],"id":148}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["_"],"id":149}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["s"],"id":150}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["r"],"id":151}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["v"],"id":152}],[{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"remove","lines":["_"],"id":153}],[{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"remove","lines":["s"],"id":154}],[{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"remove","lines":["r"],"id":155}],[{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"remove","lines":["v"],"id":156}],[{"start":{"row":12,"column":12},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":157}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":158}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["r"],"id":159}],[{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":["o"],"id":160}],[{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"insert","lines":["s"],"id":161}],[{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"insert","lines":["p"],"id":162}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["y"],"id":163}],[{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["."],"id":164}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["s"],"id":165}],[{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["p"],"id":166}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["i"],"id":167}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["n"],"id":168}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["o"],"id":169}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["o"],"id":170}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["."],"id":171}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["."],"id":172}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":10},"action":"remove","lines":["spin"],"id":173},{"start":{"row":14,"column":6},"end":{"row":14,"column":12},"action":"insert","lines":["spin()"]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":60},"action":"remove","lines":["execBB8 = rospy.ServiceProxy('/move_bb8_in_square', Empty())"],"id":180}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":60},"action":"insert","lines":["execBB8 = rospy.ServiceProxy('/move_bb8_in_square', Empty())"],"id":181}],[{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"remove","lines":[")"],"id":182}],[{"start":{"row":8,"column":57},"end":{"row":8,"column":59},"action":"remove","lines":["()"],"id":183}],[{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"insert","lines":[")"],"id":184}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["#"],"id":185}],[{"start":{"row":10,"column":17},"end":{"row":10,"column":24},"action":"remove","lines":["request"],"id":186}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":17},"end":{"row":10,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1544530750160,"hash":"4207559c2a8fa8cb2bc0ccc81ac512f46b3397b2"}