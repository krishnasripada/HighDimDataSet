function answer_17()
n = 300;
score = [];
for alpha=5:70
    for beta=1:50
        p = alpha/n;
        q = beta/n;
        meanOverlap = 0;
        if p>=q
           for i=1:20
               I = eye(n);
               ix = randperm (n);
               T = I(ix,:);
               overlp = answer_15(p,q,n,T);
               meanOverlap = meanOverlap + overlp;
           end
           score(alpha,beta) =  meanOverlap/20;
        end
       
        
    end
end
imagesc(score);
colorbar;
colormap(gray);
hold on;
for b=1:50
    p = [1 -((2*b)+1) +((b*b)-b)];
    r = roots(p);
    X(b) = r(1);
end
plot(1:b,X,'r','LineWidth',3)