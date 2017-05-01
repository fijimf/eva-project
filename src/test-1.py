import time

def request_url(api_key, bus_line, bus_stop_id):
    return 'http://api.prod.obanyc.com/api/siri/stop-monitoring.json?key={0}&version=2&LineRef={1}&MonitoringRef={2}'.format(api_key,bus_line,bus_stop_id)

while (1==1):
    url = request_url('7a7ab7fb-0edb-4b4f-9014-afca06aab8fd','MTA%20NYCT_M4','400676')
    print (url)
    time.sleep (15)