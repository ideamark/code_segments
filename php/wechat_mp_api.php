<?php
/**
  * WeChat MP API
  */

// defind your token
define("TOKEN", "Mark_Young");
$wechatObj = new wechatCallbackapiTest();
$wechatObj->valid();
//$wechatObj->responseMsg();

class wechatCallbackapiTest
{
	public function valid()
    {
        $echoStr = $_GET["echostr"];

        //valid signature , option
        if($this->checkSignature()){
        	echo $echoStr;
        	exit;
        }
    }

    public function responseMsg()
    {
		//get post data, May be due to the different environments
		$postStr = $GLOBALS["HTTP_RAW_POST_DATA"];

      	//extract post data
		if (!empty($postStr)){
            $postObj = simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);
            $resultStr = $this->handleText($postObj);
            echo $resultStr;
        }else {
        	echo "";
        	exit;
        }
    }
		
	private function checkSignature()
	{
        $signature = $_GET["signature"];
        $timestamp = $_GET["timestamp"];
        $nonce = $_GET["nonce"];	

		$token = TOKEN;
		$tmpArr = array($token, $timestamp, $nonce);
		sort($tmpArr);
		$tmpStr = implode( $tmpArr );
		$tmpStr = sha1( $tmpStr );
		
		if( $tmpStr == $signature ){
			return true;
		}else{
			return false;
		}
	}

    private function responseText($object, $content, $flag=0)
    {
        $textTpl = "<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    <FuncFlag>%d</FuncFlag>
                    </xml>";
        $resultStr = sprintf($textTpl, $object->FromUserName, $object->ToUserName, time(), $content, $flag);
        return $resultStr;
    }

    private function handleText($postObj)
    {
        $keyword = trim($postObj->Content);

		if(!empty($keyword))
        {
            try {
                $userID = " \"".$postObj->FromUserName."\" ";
                $keyword = " \"".$keyword."\" ";
        	    $responseStr = exec("python /var/www/html/python/main.py ".$userID.$keyword);
                $resultStr = $this->responseText($postObj, $responseStr);
			    $this->writeLog($postObj, $keyword, $responseStr);
            } catch (Exception $e) {
			    $resultStr = $e->getMessage();
            }
        }else{
			$resultStr = "Input something...";
        }
        return $resultStr;
    }

	private function writeLog($object, $userSaid, $response)
	{
        if ($object->FromUserName!="ot-0qxExJbukKrvtPmLDXVJ5vkPM") {
    		// Write the chat log
    		$fp = fopen("log/dialogue.txt","a");
    		$myLog = "[User] ".$object->FromUserName."\n[Time] ".date('Y-m-d H:i:s',time())."\n[User Said] ".$userSaid."\n[Response] ".$response."\n\n";
    		fwrite($fp,$myLog);
    		fclose($fp);
        }
	}

}

?>
