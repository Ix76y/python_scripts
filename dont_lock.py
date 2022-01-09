# This script has the sole purpose of letting your computer think that it is used, so it doesn't lock the screen 
import time


def dont_sleep(sleep_time, stay_busy):
  print("Keeping busy", end="")
  start_time = time.time()
  while (time.time() - start_time) > (stay_busy * 60):
    time.sleep(sleep_time)
    pag.press('volumedown')
    time.sleep(sleep_time)
    pag.press('volumeup')
    print('.', end='')
    
  print('Program ended.')
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--sleep', type=int, default=30, help='Optional Sleep time in seconds')
  parser.add_argument('-b', '--stayBusy', type=int, default=60, help='Optional time in minutes to stay busy')
  args = parser.parse_args()
  print(f'Running for {args.stayBusy} minutes.').
  dont_sleep(args.sleep, args.stayBusy)
    
