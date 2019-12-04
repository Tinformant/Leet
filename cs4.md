Question 1
For PDF or CDF is about the probability of random variables within a certain range. It is meaningless to analyze a critical condition. 

Question 2
```matlab
Num Data = 250000; 
I0 = 1; 
V0 = 1;

Data R = rand(Num Data,1) + 1;
Data C = 3.5 * rand(Num Data,1) + 1.5;
Data L = exprnd(2,[Num Data,1]) + 1;

Data alpha = Data R./(2.*Data L);
Data omega = 1./sqrt(Data C.*Data L);

Data = Data alpha - Data omega;
Data(Data<0)=0; % underdamped
Data(Data>0)=1; % overdamped

fprintf('the probability of overdamped system is %fnn', sum(Data)/Num Data);
fprintf('the probability of underdamped system is %fnn', (Num Data-sum(Data))/Num Data);
```
