function [overlap] = answer_15(p,q,n,T)

adjMatrixT = adjMatrix(1,0,n,T);
[V,D] = eig(adjMatrixT);
[X,Y] = sort(max(abs(D)), 'descend');
secondDEVT = V(:,Y(2));
for i=1:numel(secondDEVT)
    element = abs(secondDEVT(i));
    if element+1 ~=1
        wT(i) = 1;
    else
        wT(i) = -1;
    end
end

adjMatrixR = adjMatrix(p,q,n,T);
[V,D] = eig(adjMatrixR);
[X,Y] = sort(max(abs(D)), 'descend');
secondDEVR = V(:,Y(2));
for i=1:numel(secondDEVR)
    element = secondDEVR(i);
    if element>0
        wR(i) = 1;
    else
        wR(i) = -1;
    end
end
rawoverlap = max(sum(wT==wR), sum(-wT==wR));
overlap = (2*(rawoverlap)/n) - 1;
end

