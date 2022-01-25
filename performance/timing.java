int frames=0, maxFrames=10000;
float time=0;



frames++;
time+=delta;
if(frames%1000==0)System.out.println(frames);
if(frames>=maxFrames){
  try {
    new FileOutputStream("F:/Daten/OneDrive/OTH/Master/MI4/Masterarbeit/performancetiming.txt", true).write(("CONFIG: \t"+time+"\r\n").getBytes(StandardCharsets.UTF_8));
  } catch (IOException e) {
    e.printStackTrace();
  }
  break;
}