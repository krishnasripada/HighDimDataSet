function [ overlp ] = answer_19(partition1, partition2, n)
rawoverlap = max(sum(partition1==partition2), sum(-partition1==partition2));
overlp = (2*(rawoverlap)/n) - 1;
end