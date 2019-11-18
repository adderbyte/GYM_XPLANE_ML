-- first we need ffi module (variable must be declared local)
local ffi = require("ffi")
--local sh = require('sh')
--local xdotool = require('xdotool')
-- find the right lib to load
local XPLMlib = ""
if SYSTEM == "IBM" then
  -- Windows OS (no path and file extension needed)
  if SYSTEM_ARCHITECTURE == 64 then
    XPLMlib = "XPLM_64"  -- 64bit
  else
    XPLMlib = "XPLM"     -- 32bit
  end
elseif SYSTEM == "LIN" then
  -- Linux OS (we need the path "Resources/plugins/" here for some reason)
  if SYSTEM_ARCHITECTURE == 64 then
    XPLMlib = "Resources/plugins/XPLM_64.so"  -- 64bit
  else
    XPLMlib = "Resources/plugins/XPLM.so"     -- 32bit
  end
elseif SYSTEM == "APL" then
  -- Mac OS (we need the path "Resources/plugins/" here for some reason)
  XPLMlib = "Resources/plugins/XPLM.framework/XPLM" -- 64bit and 32 bit
else
  return -- this should not happen
end

-- load the lib and store in local variable
local XPLM = ffi.load(XPLMlib)

-- define the XPLMReloadScenery() C-function to be used from Lua
ffi.cdef( "void XPLMReloadScenery(void)" )
-- ffi.cdef("int   XPLMGetMyID(void)")




-- collect variables in dictionary, this allows
-- tracking scope of variables
controlVariables = { ["closeScenery_flag"] = true,
["count"] = 0,
["counter_check"] = 90,
["scenery_restart"] = true


}

-- function to get count 
function get_count(count)  
  if count < controlVariables.counter_check then
    count = count + 1
  elseif count >= controlVariables.counter_check then
    count = 0 
  end

  logMsg(count)  -- for debugging
  return count

end

-- function to sleep for a while 
-- from stack overflow
local clock = os.clock
function sleeps(n)  -- seconds
  local t0 = clock()
  while clock() - t0 <= n do end
end


--DataRef("yp", "sim/cockpit2/controls/yoke_pitch_ratio")
--DataRef("yr", "sim/cockpit2/controls/yoke_roll_ratio")
--DataRef("sb", "sim/cockpit2/controls/speedbrake_ratio")
--DataRef("fr", "sim/cockpit2/controls/flap_ratio")
--DataRef("ws", "sim/cockpit2/controls/wingsweep_ratio")
DataRef("ground", "sim/flightmodel2/gear/on_ground")

DataRef("crasher", "sim/flightmodel/engine/ENGN_running",0)
DataRef("gear", "sim/cockpit/switches/gear_handle_status", "writable")
gear=0.0
logMsg("Target height ...",gear )

command_once("sim/autopilot/hsi_select_gps")
set("sim/cockpit/switches/gear_handle_status", 0) -- set gear status to zero since not landing


-- define local function
function let_XPLM_reload_the_scenery() 
    --[[  This function reloads the scene if the 
	  count is less than countercheck.
	 The command do_often runs this function often
	on the frame. Try do_sometimes or do_every_frame
	The add_macro puts makes it possible to set this 
	function as macro on xplane under the flyWithLua menu
    ]]
   	
   if ground >= 1  then
	logMsg(controlVariables.count)
        controlVariables.count = 0
        logMsg("I am ground")
	print("reloading")
	--sleeps(2)
	--command_once('sim/FMS/next')
	--command_once('sim/FMS2/next')
	--WID='xdotool search' --title "X-System" | head -1`
	--xdotool windowfocus $WID
	--xdotool key ctrl+V	
	--reload_scenery()
        -- this XPLM.XPLMReloadScenery()
    	---XPLMSpeakString("X Plane reloading")
        load_situation(SYSTEM_DIRECTORY .. "/Output/situations/keepHeading.sit" )

	--XPLM.XPLMReloadScenery()
	end	
	
	

   
  
	 
   if crasher<=0  then
	logMsg(controlVariables.count)
        controlVariables.count = 0
        logMsg("I am crasher")
	print("reloading")
	--sleeps(2)
	--command_once('sim/FMS/next')
	--command_once('sim/FMS2/next')
	--WID='xdotool search' --title "X-System" | head -1`
	--xdotool windowfocus $WID
	--xdotool key ctrl+V	
	--reload_scenery()
        -- this XPLM.XPLMReloadScenery()
    	---XPLMSpeakString("X Plane reloading")
        load_situation(SYSTEM_DIRECTORY .. "/Output/situations/keepHeading.sit" )

	--XPLM.XPLMReloadScenery()
	end
	
   if controlVariables.count >= controlVariables.counter_check  then 
	logMsg(controlVariables.count)
        logMsg("I am control")
	--sleeps(1)
	--XPLM.XPLMReloadScenery()
	controlVariables.count = get_count(controlVariables.count)
	--command_once('sim/FMS/next')
	--command_once('sim/FMS2/next')
	--WID='xdotool search' --title "X-System" | head -1`
	--xdotool windowfocus $WID
	--xdotool key ctrl+V	
	--reload_scenery()
        -- this XPLM.XPLMReloadScenery()
    	---XPLMSpeakString("X Plane reloading")
	load_situation(SYSTEM_DIRECTORY .. "/Output/situations/keepHeading.sit" )
	--XPLM.XPLMReloadScenery()
        --logMsg(count)
	--XPLM.XPLMReloadScenery()
    else 
	--command_once('sim/FMS2/next')
	--command_once('sim/FMS2/next')
        
	logMsg("I am counter altitude")
       
       
        --print(ground)
        --print(crasher)
        controlVariables.count = get_count(controlVariables.count)
	 --if  controlVariables.count == 1 and controlVariables.scenery_restart then
		--load_situation(SYSTEM_DIRECTORY .. "/Output/situations/cruise.sit" )
	--end	
   end    
	--load_aircraft()
	
  --[[ elseif count < 4 then
        --flag = true
        
        command_once('sim/operation/close_windows')
        count = sleep(count)
        XPLMSpeakString("Running check check ...") 
 
  end]]
 
end

do_often("let_XPLM_reload_the_scenery()")


--if count < counter_check then
 --add_macro("Reloader", "autopilot_helper_active = true", "autopilot_helper_active = false", "activate")
 --add_macro("Reloader", "autopilot_helper_active = true", "autopilot_helper_active = false", "deactivate")
if controlVariables.count >= controlVariables.counter_check then 
    add_macro("Reloader", "closeScenery_flag = true", "closeScenery_flag = false", "activate")
  --else
   --add_macro("Reloader", "autopilot_helper_active = true", "autopilot_helper_active = false", "deactivate")
end








