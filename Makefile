service = wrk
version = $(shell git describe --long --tags --dirty | awk '{print substr($$1,2)}')
build_dir = _build

rpm_dir = $(build_dir)/rpm
rpm_version = $(shell echo $(version) | sed -nr "s/^([0-9]+(\.[0-9]+)+)(-([-A-Za-z0-9\.]+))?$$/\1/p")
rpm_release = $(subst -,.,$(shell echo $(version) | sed -nr "s/^([0-9]+(\.[0-9]+)+)(-([-A-Za-z0-9\.]+))?$$/\4/p"))
.PHONY: docker-rpm
docker-rpm:
	mkdir -p $(rpm_dir)
	cp $(service)* $(rpm_dir)
	git log --format="* %cd %aN%n- (%h) %s%d%n" -n 10 --date local \
			| sed -r 's/[0-9]+:[0-9]+:[0-9]+ //' >> $(rpm_dir)/$(service).spec
	chmod -R g+w,o+w $(rpm_dir)
	docker run --privileged --rm -v $(shell pwd)/$(rpm_dir):/home/builder/rpm \
			-w /home/builder/rpm rpmbuild/centos7 \
			rpmbuild --define '_name $(service)' --define '_version $(rpm_version)' \
			--define '_release $(rpm_release)' --define '_source $(release_name)' -bb $(service).spec
