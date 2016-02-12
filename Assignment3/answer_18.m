function [wR] = answer_18(filename)
X = load(filename);
[V,D] = eig(X.A);
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
end

