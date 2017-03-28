
# This script loop over the 6th first panels
# and plot the result of dichotomization exploration
# using cross validation.



for(i in 1:6) {
  
  #set variables
  file_name = paste("/home/foulquier/Bureau/SpellCraft/WorkSpace/Github/GUI/data/dichotomization_exploration_panel_",i,".log", sep="")
  save_name = paste("/home/foulquier/Bureau/SpellCraft/WorkSpace/Github/GUI/images/dichotomization_exploration_panel_",i,".png", sep="")
  plot_title = paste("Panel ",i, sep="")
  
  # Load data
  flow_data <- read.csv(file_name, header = F, stringsAsFactors = F, sep=";")
  
  # prepare to save the plot
  png(filename=save_name)
  
  # Plot data
  plot(flow_data, type="o", col="blue", ann=FALSE)
  
  # Label the x and y axes
  title(xlab="number of intervals")
  title(ylab="score")
  
  # write title
  title(main=plot_title)
  
  #stop recording
  dev.off()
  
}
